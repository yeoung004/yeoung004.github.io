# INNER JOIN / WHERE 차이

> 동료의 코드를 보다 INNER JOIN과 WHERE을 혼용해서 사용하길래 어떤것이 더 좋은 코드인지 궁금해서 찾아보기로 했고 이부분을 적용하였다.

먼저 JOIN과 WHERE의 퍼포먼스 측면에서는 동일했다. 계속 사용해도 뭔가 하나 특별히 좋은 지도 몰랐었지만, 코드가 길어지면 길어질수록 쿼리가 복잡하면 복잡할수록 WHERE과 테이블을 JOIN하는 코드가 멀어져서 결국 혼용해서 사용하면 어떤 조건이 들어가 있는지 한눈에 읽기 힘들다는 것을 느꼈다. <br />

그래서 다른 사람의 의견을 참고하여 쿼리문이 싱글 테이블 일 경우 WHERE을 사용, 멀티 테이블일 경우 INNER JOIN을 사용하기로 컨벤션을 정했다.

`아래 코드는 동료가 개발한 코드다`

```
SELECT ai.brand,
       ai.model,
       ai.pattern,
       ai.min_bid,
       b.name_image,
       im.image,
       ga.idx,
       ga.start_dt,
       ga.finish_dt,
       ai.size,
       ai.special_gift,
       b.white_name
FROM auction_info ai
         INNER JOIN goods g ON ai.goods_idx = g.idx
         INNER JOIN item i ON g.item_idx = i.idx
         INNER JOIN model m ON i.model_idx = m.idx
         INNER JOIN brand b ON m.brand_code = b.code
         INNER JOIN auction_image im ON im.auction_info_idx = ai.idx
         INNER JOIN goods_auction ga ON ai.idx = ga.auction_info_idx
WHERE im.type = 'MF'
  AND g.status = 'A005'
  AND ga.is_ready_active = 1
  AND ga.start_dt IS NOT NULL
  AND ga.start_dt >= now()
ORDER BY ga.start_dt ASC
LIMIT 5;
```

`아래 코드는 WHERE 조건을 전부 INNER JOIN으로 옮겼다`

```
SELECT CONCAT(ai.model, ' ', ai.pattern, ' ', ai.size) as name,
              ai.min_bid as minBbd,
              b.name_image as nameImage,
              im.image,
              ga.idx,
              ga.start_dt as startDt,
              ga.finish_dt as finishDt,
              ai.size,
              ai.special_gift as specialGift,
              b.white_name as whiteName
       FROM auction_info ai
            INNER JOIN goods g
                   ON ai.goods_idx = g.idx AND g.status = 'A005'
            INNER JOIN item i ON g.item_idx = i.idx
            INNER JOIN model m ON i.model_idx = m.idx
            INNER JOIN brand b ON m.brand_code = b.code
            INNER JOIN auction_image im
                   ON im.auction_info_idx = ai.idx
                   and im.type = 'MF'
            INNER JOIN goods_auction ga
                   ON ai.idx = ga.auction_info_idx
                   AND ga.is_ready_active = 1
                   AND ga.start_dt IS NOT NULL
                   AND ga.start_dt >= now()
       ORDER BY ga.start_dt ASC
       LIMIT 5
```

물론 둘중 어떤 조건식을 주어도 동일한 결과와 동일한 퍼포먼스가 나오겠지만, 지속가능한 코드를 위해 가독성을 먼저 생각하는 내 스타일로는 이 방식이 더 잘맞는듯 하다.


# What is different between "INNER JOIN" and WHERE in mariaDB

> I was reading my coworker's query code suddenly I was curios what is more better code between INNER JOIN and WHERE so I looked up and I changed code convention about this part.

First, JOIN and WHERE are equal performance. so I didn't know what is better code before I read complicated query. When I try to read complicated query source, I realized it when I read complicated code.<br />

Therefore, referring to the opinions of others, I got dcided to use WHERE if the query statement was a single table and INNER JOIN if it was a multi-table.

`This is the coworker's code`


```
SELECT ai.brand,
       ai.model,
       ai.pattern,
       ai.min_bid,
       b.name_image,
       im.image,
       ga.idx,
       ga.start_dt,
       ga.finish_dt,
       ai.size,
       ai.special_gift,
       b.white_name
FROM auction_info ai
         INNER JOIN goods g ON ai.goods_idx = g.idx
         INNER JOIN item i ON g.item_idx = i.idx
         INNER JOIN model m ON i.model_idx = m.idx
         INNER JOIN brand b ON m.brand_code = b.code
         INNER JOIN auction_image im ON im.auction_info_idx = ai.idx
         INNER JOIN goods_auction ga ON ai.idx = ga.auction_info_idx
WHERE im.type = 'MF'
  AND g.status = 'A005'
  AND ga.is_ready_active = 1
  AND ga.start_dt IS NOT NULL
  AND ga.start_dt >= now()
ORDER BY ga.start_dt ASC
LIMIT 5;
```

`so I changed like this`

```
SELECT CONCAT(ai.model, ' ', ai.pattern, ' ', ai.size) as name,
              ai.min_bid as minBbd,
              b.name_image as nameImage,
              im.image,
              ga.idx,
              ga.start_dt as startDt,
              ga.finish_dt as finishDt,
              ai.size,
              ai.special_gift as specialGift,
              b.white_name as whiteName
       FROM auction_info ai
            INNER JOIN goods g
                   ON ai.goods_idx = g.idx AND g.status = 'A005'
            INNER JOIN item i ON g.item_idx = i.idx
            INNER JOIN model m ON i.model_idx = m.idx
            INNER JOIN brand b ON m.brand_code = b.code
            INNER JOIN auction_image im
                   ON im.auction_info_idx = ai.idx
                   and im.type = 'MF'
            INNER JOIN goods_auction ga
                   ON ai.idx = ga.auction_info_idx
                   AND ga.is_ready_active = 1
                   AND ga.start_dt IS NOT NULL
                   AND ga.start_dt >= now()
       ORDER BY ga.start_dt ASC
       LIMIT 5
```

Of course, any conditional expression of the two will produce the same result and the same performance, but this method seems to fit better with my style of thinking about readability first for sustainable code.

