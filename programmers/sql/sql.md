##### ORDER BY = 정렬

1. ASC : 오름차순
2. DESC : 내림차순

<br />

##### 문자열
1. 문자열 검색
    ```
    WHERE 컬럼명 like '강원도%'
    ```
2. 부분 문자열
    ```
    SUBSTR(B.CREATED_DATE,1,7) = '2022-10'
    ```
<br />

##### JOIN문
```
SELECT * <br />
FROM BOARD AS A <br />
JOIN REPLY AS B <br />
ON A.id = B.id
```

<br />

##### 날짜
1. 포맷 변경
    ```
    DATE_FORMAT('2022-12-03 00:00:00', '%Y-%m-%d')
    ```
2. 