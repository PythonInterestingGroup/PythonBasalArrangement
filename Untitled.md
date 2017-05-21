
```xml
group:android.permission-group.CONTACTS
permission:android.permission.WRITE_CONTACTS
permission:android.permission.GET_ACCOUNTS
permission:android.permission.READ_CONTACTS
 
group:android.permission-group.PHONE
permission:android.permission.READ_CALL_LOG
permission:android.permission.READ_PHONE_STATE
permission:android.permission.CALL_PHONE
permission:android.permission.WRITE_CALL_LOG
permission:android.permission.USE_SIP
permission:android.permission.PROCESS_OUTGOING_CALLS
permission:com.android.voicemail.permission.ADD_VOICEMAIL
 
group:android.permission-group.CALENDAR
permission:android.permission.READ_CALENDAR
permission:android.permission.WRITE_CALENDAR
 
group:android.permission-group.CAMERA
permission:android.permission.CAMERA
 
group:android.permission-group.SENSORS
permission:android.permission.BODY_SENSORS
 
group:android.permission-group.LOCATION
permission:android.permission.ACCESS_FINE_LOCATION
permission:android.permission.ACCESS_COARSE_LOCATION
 
group:android.permission-group.STORAGE
permission:android.permission.READ_EXTERNAL_STORAGE
permission:android.permission.WRITE_EXTERNAL_STORAGE
 
group:android.permission-group.MICROPHONE
permission:android.permission.RECORD_AUDIO
 
group:android.permission-group.SMS
permission:android.permission.READ_SMS
permission:android.permission.RECEIVE_WAP_PUSH
permission:android.permission.RECEIVE_MMS
permission:android.permission.RECEIVE_SMS
permission:android.permission.SEND_SMS
permission:android.permission.READ_CELL_BROADCASTS

```
##requestPermissions
  
```java
	public static void requestPermissions(final @NonNull Activity activity,
            final @NonNull String[] permissions, final @IntRange(from = 0) int requestCode) {
        if (Build.VERSION.SDK_INT >= 23) {
            ActivityCompatApi23.requestPermissions(activity, permissions, requestCode);
        } else if (activity instanceof OnRequestPermissionsResultCallback) {
            Handler handler = new Handler(Looper.getMainLooper());
            handler.post(new Runnable() {
                @Override
                public void run() {
                    final int[] grantResults = new int[permissions.length];

                    PackageManager packageManager = activity.getPackageManager();
                    String packageName = activity.getPackageName();

                    final int permissionCount = permissions.length;
                    for (int i = 0; i < permissionCount; i++) {
                        grantResults[i] = packageManager.checkPermission(
                                permissions[i], packageName);
                    }

                    ((OnRequestPermissionsResultCallback) activity).onRequestPermissionsResult(
                            requestCode, permissions, grantResults);
                }
            });
        }
    }  
...  

    public static void requestPermissions(Activity activity, String[] permissions,
            int requestCode) {
        if (activity instanceof RequestPermissionsRequestCodeValidator) {
            ((RequestPermissionsRequestCodeValidator) activity)
                    .validateRequestPermissionsRequestCode(requestCode);
        }
        activity.requestPermissions(permissions, requestCode);
    }  
    
...

    @Override
    public final void validateRequestPermissionsRequestCode(int requestCode) {
        // We use 16 bits of the request code to encode the fragment id when
        // requesting permissions from a fragment. Hence, requestPermissions()
        // should validate the code against that but we cannot override it as
        // we can not then call super and also the ActivityCompat would call
        // back to this override. To handle this we use dependency inversion
        // where we are the validator of request codes when requesting
        // permissions in ActivityCompat.
        if (!mRequestedPermissionsFromFragment
                && requestCode != -1) {
            checkForValidRequestCode(requestCode);
        }
    }  
    
...
    
    public final void requestPermissions(@NonNull String[] permissions, int requestCode) {
        if (mHasCurrentPermissionsRequest) {
            Log.w(TAG, "Can reqeust only one set of permissions at a time");
            // Dispatch the callback with empty arrays which means a cancellation.
            onRequestPermissionsResult(requestCode, new String[0], new int[0]);
            return;
        }
        Intent intent = getPackageManager().buildRequestPermissionsIntent(permissions);
        startActivityForResult(REQUEST_PERMISSIONS_WHO_PREFIX, intent, requestCode, null);
        mHasCurrentPermissionsRequest = true;
    }
```