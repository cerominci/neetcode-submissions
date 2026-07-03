class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        # Deque to store indices of elements in decreasing order
        # The front of the deque will always store the index of the maximum element
        # in the current effective window.
        dq = collections.deque()
        
        left = 0 # Left pointer of the sliding window

        for right in range(len(nums)):
            # 1. Remove elements from the back of the deque if they are smaller
            #    than or equal to the current element.
            #    This ensures that dq stores indices of elements in decreasing order.
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()
            
            # 2. Add the current element's index to the back of the deque.
            dq.append(right)

            # 3. Remove elements from the front of the deque if they are out of the current window.
            #    The element at dq[0] is always the largest in the relevant part of the window.
            #    If its index is less than the current window's start (left), it's no longer relevant.
            if dq[0] < left:
                dq.popleft()
            
            # 4. If the window has reached size k (or is larger, for the initial phase),
            #    the maximum for the current window is at the front of the deque.
            if right >= k - 1: # This condition simplifies checking window size
                result.append(nums[dq[0]])
                # Move the left pointer to slide the window
                left += 1 
                # Note: We don't explicitly remove left from deque here;
                # it's handled by the 'dq[0] < left' check in the next iteration.

        return result


            