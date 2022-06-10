# Nginx에서 자주 하는 열 가지 실수들

From: [Nginx Blog](https://www.nginx.com/blog/avoiding-top-10-nginx-configuration-mistakes/)



1. worker 당 부족한 file descriptors





# 실수 1: 부족한 File Descriptor

`worker_connections`에는 NGINX의 한 worker process가 열 수 있는 최대 동시 connection 수가 정의됩니다. 기본값은 512이며, 여기서 connection이란 외부 client의 연결뿐만 아니라 모든 종류의 연결을 의미합니다.

그런데, NGINX의 각 process에는 OS가 제한하는 최대 File Descriptor (FD) 할당 갯수 또한 설정됩니다. 현재 대부분의 UNIX 배포에서 이 값은 1024로 설정됩니다.

여기서 자주 저지르는 실수는, 필요에 따라 `worker_connections`의 값을 증가시켰지만 FD 의 값은 그대로 놔두는 경우입니다. worker_connections의 2배수가 되도록 **`worker_rlimit_nofile`**설정값을 바꾸는 것이 권장됩니다. 



# 실수 2: `error_log off`

`access_log` directive와 달리 `error_log`는 `off` 파라메터를 받지 않습니다.

`error_log off`라는 설정은 로그를 작성하지 않는 옵션이 아니라, 에러 로그를 기본 폴더의 `off`라는 파일로 작성다겠다는 의미가 됩니다.

에러 로그를 비활성화하는 것은 일반적으로 권장되지 않지만, 특이한 경우 (i.e. 저장장치 공간이 매우 협소한 경우) 로그를 다음과 같이 비활성화할 수 있습니다.

```
error_log /dev/null emerg;
```

NGINX가 해당 설정을 읽기 전까지는 로그 작성이 이루어지므로, 이 명렁어에도 불구하고 여전히 `var/log/nginx/error.log` 등 기본 로그 위치에 에러 로그가 작성이 될 수도 있습니다.



# 실수 3: Upstream  서버들에 Keepalive Connections 비활성화

기본적으로 NGINX는 모든 요청에 대해 upstream 서버에 새 연결을 열게 되어 있습니다. 하지만 이런 구조는 서버 리소스를 과하게 사용하는 문제를 일으킵니다. 



# 실수 5: `proxy_buffering off`



# 실수 6: `if` 잘못 사용하기



# 실수 7: 과도한 상태 체크 Health Check





# 실수 8: 



# 실수 9: 

# 실수 10: Upstream 활용하지 않기