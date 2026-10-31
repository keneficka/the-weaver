#!/usr/bin/env python3
"""
Data Streams - Pipeline Processor
Weaving data transformation streams through the digital loom...
"""

import json
import os
import re
from collections import defaultdict
from datetime import datetime

class StreamWeaver:
    """Main class for weaving data stream pipelines"""
    
    def __init__(self):
        self.pipeline_stages = []
        
    def add_stage(self, name, processor_func):
        """Add a processing stage to the pipeline"""
        self.pipeline_stages.append((name, processor_func))
    
    def weave_stream(self, data_source, source_type='dict'):
        """Weave a stream of data through all stages"""
        
        if source_type == 'dict':
            # Single data item - replicate for processing
            if not isinstance(data_source, (list, tuple)):
                data_list = [data_source]
            else:
                data_list = list(data_source)
        elif source_type == 'file':
            with open(data_source, 'r') as f:
                content = json.load(f)
                if isinstance(content, dict):
                    data_list = [content]
                else:
                    data_list = content
        elif source_type == 'generator':
            data_list = list(data_source)
        
        # Process through pipeline stages
        results = []
        for item in data_list:
            processed = item
            for stage_name, processor in self.pipeline_stages:
                try:
                    processed = processor(processed)
                except Exception as e:
                    processed['_error'] = str(e)
            
            results.append({
                'original': item,
                'processed': processed,
                'timestamp': datetime.now().isoformat()
            })
        
        return results
    
    def filter_stage(self, predicate):
        """Create a filtering stage that keeps items matching predicate"""
        def processor(item):
            if predicate(item):
                return {'_filter': 'kept', **item}
            else:
                return None
        return processor
    
    def transform_stage(self, key_name, transform_func):
        """Create a transformation stage for a specific key"""
        def processor(item):
            if key_name in item:
                result = {key_name: transform_func(item[key_name]), **item}
            else:
                result = {'_note': f'Key {key_name} not found'}, item
            return result
        return processor
    
    def enrich_stage(self, field_name):
        """Add timestamp to each record"""
        def processor(item):
            if '_timestamp' not in item:
                item['_timestamp'] = datetime.now().isoformat()
            return item
        return processor

def main():
    """Demonstrate data stream weaving capabilities"""
    
    weaver = StreamWeaver()
    
    # Define pipeline stages
    weaver.add_stage('enrich', weaver.enrich_stage('_timestamp'))
    weaver.add_stage('normalize_numeric', lambda item: {k: float(v) if isinstance(v, (int, float)) else v for k, v in item.items()} if '_error' not in item else item)
    weaver.add_stage('validate_strings', lambda item: {k: str(v) if not isinstance(v, str) else v for k, v in item.items() if k not in ['_timestamp', '_error'] and '_filter' not in item} if '_error' not in item else item)
    weaver.add_stage('filter_null_keys', lambda item: {'_filter': 'removed'} if any(v is None for k, v in item.items()) else item)
    
    # Sample data to process
    sample_data = [
        {'id': 1, 'name': 'Alice', 'age': 30, 'city': 'London'},
        {'id': 2, 'name': 'Bob', 'age': 'twenty-five', 'city': None},
        {'id': 3, 'name': 'Charlie', 'age': 35, 'city': 'Paris'},
    ]
    
    print("Data Stream Weaver")
    print("=" * 50)
    
    # Weave the stream through pipeline
    results = weaver.weave_stream(sample_data, source_type='dict')
    
    print(f"\nProcessed {len(results)} records through pipeline:")
    for result in results:
        print(f"  Record {result['original']['id']}:")
        print(f"    Processed: {result['processed']}")
    
    # Save processed data to file
    output_dir = 'projects/network_threads/data_streams/output'
    os.makedirs(output_dir, exist_ok=True)
    
    # Filter out records that were filtered/removed
    valid_records = [r['processed'] for r in results if '_filter' not in r or r.get('_filter') == 'kept']
    
    output_file = os.path.join(output_dir, 'processed_stream.json')
    with open(output_file, 'w') as f:
        json.dump(valid_records, f, indent=2)
    
    print(f"\nProcessed records saved to {output_file}")

if __name__ == '__main__':
    main()
