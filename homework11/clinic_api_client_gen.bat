set executable=.\tools\swagger-codegen-cli.jar


REM set JAVA_OPTS=%JAVA_OPTS% -Xmx1024M
set ags=generate -i http://127.0.0.1:8000/openapi.json -l python -o clinic_client\ -DpackageName=clinic_api

java %JAVA_OPTS% -jar %executable% %ags%
