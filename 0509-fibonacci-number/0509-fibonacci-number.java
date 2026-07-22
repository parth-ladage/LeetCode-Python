class Solution {
    public int fib(int n) {
        // if (n<=1) return n;
        // return fib(n-1) + fib(n-2);

        int first = 0;
        int second = 1;
        for ( int i=1; i<=n ; i++) {
            int third = first + second;
            first = second;
            second = third;
        }
        return first;
    }
}