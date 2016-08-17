
public class MergeSortedArray {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1;
        int j = n - 1;
        int cur = m + n - 1;
        while(i >= 0 && j >= 0) {
            if(nums1[i] >= nums2[j]) {
                nums1[cur] = nums1[i];
                i--;
            } else {
                nums1[cur] = nums2[j];
                j--;
            }
            cur--;
        }
        while(i >= 0) {
            nums1[cur] = nums1[i];
            i--;
            cur--;
        }
        while(j >= 0) {
            nums1[cur] = nums2[j];
            j--;
            cur--;
        }
    }

}
