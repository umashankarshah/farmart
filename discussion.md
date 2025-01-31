# Log Extraction Solution

## Solutions Considered

### 1. Simple Line-by-Line Reading
- **Approach:** Read the entire file line by line and filter by date.
- **Drawbacks:** 
  - Extremely slow for large files (1 TB)
  - High memory consumption
  - Not scalable for big data scenarios

### 2. Memory Mapping (Chosen Solution)
- **Approach:** Use memory mapping to efficiently read large files
- **Advantages:**
  - O(n) time complexity
  - Low memory overhead
  - Direct file access without loading entire file
  - Works efficiently with very large files

### 3. Indexed Approach (Alternative)
- **Potential Solution:** Pre-build an index mapping dates to file offsets
- **Trade-offs:**
  - Faster for repeated queries
  - Initial indexing overhead
  - Additional storage required

## Final Solution Summary

### Implementation Strategy
- Use Python's `mmap` module for efficient file reading
- Memory-map the entire file
- Scan through file line by line
- Extract and write matching log entries

### Key Optimizations
- Minimal memory usage
- Direct file access
- Simple, linear scanning
- Low computational complexity

## Steps to Run

1. **Prerequisites**
   - Python 3.7+
   - Ensure `test_logs.log` is in the same directory

2. **Download Log File**
   ```bash
   curl -L -o test_logs.log "https://limewire.com/d/90794bb3-6831-4e02-8a59-ffc7f3b8b2a3#X1xnzrH5s4H_DKEkT_dfBuUT1mFKZuj4cFWNoMJGX98"
   ```

3. **Run the Script**
   ```bash
   python extract_logs.py YYYY-MM-DD
   ```
   Replace `YYYY-MM-DD` with the target date.

## Performance Considerations
- First query might be slightly slower due to file mapping
- Subsequent queries will be very fast
- Memory usage remains constant regardless of file size
