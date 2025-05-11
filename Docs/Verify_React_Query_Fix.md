# Verifying React Query Integration Fix

This document provides the steps to verify that the community membership functionality works correctly both **with** and **without** React Query integration.

---

## Testing Environments

### 1. With React Query Provider

In environments where **React Query** is properly set up:

```jsx
// In _app.jsx or equivalent
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

const queryClient = new QueryClient();

function MyApp({ Component, pageProps }) {
  return (
    <QueryClientProvider client={queryClient}>
      <Component {...pageProps} />
    </QueryClientProvider>
  );
}
```

### 2. Without React Query Provider

In environments where **React Query** is **not** set up or available:

```jsx
// In _app.jsx or equivalent
function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />;
}
```

---

## Test Cases

### Test Case 1: Join Community

1. Navigate to a community you're **not a member of**.
2. Open the browser console and check for any React Query errors.
3. Click the **"Join Community"** button.
4. Verify in the console that:

   * No React Query errors are shown.
   * The log shows: `"React Query not available for cache invalidation"` (if provider is missing).
   * The **Join operation** completes successfully.
   * The **UI updates** correctly to show the updated membership status.

### Test Case 2: Leave Community

1. Navigate to a community you're **a member of**.
2. Open the browser console and check for any React Query errors.
3. Click the **"Leave Community"** button.
4. Verify in the console that:

   * No React Query errors are shown.
   * The log shows: `"React Query not available for cache invalidation"` (if provider is missing).
   * The **Leave operation** completes successfully.
   * The **UI updates** correctly to show the updated membership status.

### Test Case 3: Network Retry with React Query

1. Enable **network throttling** in the developer tools (Slow 3G or equivalent).
2. Try to join a community.
3. Check the console logs to ensure:

   * **Retry logic** works properly (React Query should retry the operation if it fails due to network issues).
   * No React Query errors are shown, even if operations take longer.
   * **Cache invalidation** attempts are handled properly.

---

## Expected Results

### For Environments WITH React Query Provider

1. **Join/Leave** operations should work normally.
2. Cache invalidation occurs after membership changes, as shown in the logs:

   ```
   [Query] - Invalidating queries for ["community", "slug"]
   [Query] - Invalidating queries for ["membershipStatus", "slug"]
   [Query] - Invalidating queries for ["communities"]
   ```
3. No errors related to React Query should appear in the console.

### For Environments WITHOUT React Query Provider

1. **Join/Leave** operations should still work normally.
2. The console should log:

   ```
   React Query not available for cache invalidation
   ```
3. No errors related to React Query should appear in the console.
4. The **UI updates** should occur manually through state management, without cache invalidation.

---

## Troubleshooting

If issues are still encountered:

1. **Check the console** for specific error messages related to React Query or cache invalidation.
2. **Verify defensive coding** in hooks:

   * Ensure that `useQueryClient` usage is wrapped in a `try-catch`.
   * Ensure `queryClient` is **null-checked** before use.
   * Ensure cache invalidation is wrapped in a `try-catch` block to prevent crashes in the absence of the provider.
3. **Review the component tree** to ensure React Query hooks are not being used in unexpected or incorrect places (e.g., outside of a valid QueryClientProvider).

---