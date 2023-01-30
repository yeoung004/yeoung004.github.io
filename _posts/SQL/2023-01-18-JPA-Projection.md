# JPA Projection

> 서버 개발자가 나가버려 혼자인 상황에서 예전에 쓰던 MyBatis를 버리고 JPA Hibernate를 사용하는 상황에서 혼자 어찌어찌 헤쳐나가야 했다. 기존 소스를 보던중에 db를 조회해서 result를 받고 그 소스를 mapping해서 reponse를 보내주는 소스였는데 return type이 object[]로 받아와서 인덱스로 접근해 값을 가져오는데 이게 어떤 값인지를 한번에 파악하기 어려웠고 여기저기 중복 되어있는 상태여서 return type을 바꾸려던 시도해 봤지만 계속 에러만 나고 있었다. 그래서 Projection에 대해 공부했고 이 부분을 새로 적용했다.


Projection에는 여러가지 방법이 있지만 그중 시도해본 방법과 단점이 있었다.

1. POJO를 통해 가져오려면 ->
```@Query(value = "SELECT new 경로.blablaDto(blaCol, blaCol2) from blaTable")```<br />
이런식으로 해야하지만 LIMIT가 query문에 있기 때문에 JPQL로는 불가능 했다<br />
2. interface로 get함수를 만들어서 필요한 값들만 가져오기 여기서 인터페이스를 만들고 모든 컬럼에 as로 함수와 동일한 카멜케이스로 만들어야 값을 매핑해준다.
```
public interface NewAuctionItem {
    String getName();
    ...
}

List<NewAuctionItem> find5NewBids();

```

최종적으로 interface를 만들어 필요한 값만 받아오도록 수정했다.

기존 코드
```
    List<Object[]> auction5 = auctionInfoRepository.find5New();
    ArrayList<AuctionItemDto> newAuctionItems = new ArrayList();
    for(int i=0; i<auction5.size(); i++){
      AuctionItemDto newAuctionItem = new AuctionItemDto();
      Object[] row = auction5.get(i);
      newAuctionItem.setName(String.valueOf(row[1]) + " " + String.valueOf(row[2]) + " " + row[9].toString());
      newAuctionItem.setMinBid(Long.valueOf(row[3].toString()));
      newAuctionItem.setNameImage(String.valueOf(row[4]));
      newAuctionItem.setImage(row[5].toString());
      newAuctionItem.setGoodsAuctionIdx(Long.valueOf(row[6].toString()));
      newAuctionItem.setStartDt(String.valueOf(row[7]));
      newAuctionItem.setFinishDt(String.valueOf(row[8]));
      newAuctionItem.setSpecialGift(Integer.parseInt(row[10].toString()));
      newAuctionItem.setWhiteName(row[11].toString());
      newAuctionItems.add(newAuctionItem);
    }
    mainDto.setNewAuctionItems(newAuctionItems);
```

새로운 코드

```
mainDto.setNewAuctions(auctionInfoRepository.find5NewBids());
```

return 타입만 바꿨을 뿐인데 코드가 매우 간결해 지고 중복된 코드를 더 이상 넣지 않아도 됬다.
<br /><br />

--- 

<br />

# JPA Projection

> In a situation what the server developer left from work and I'm the only one developer who works at this company, I need to learn how to use JPA Hibernate.
I used to use MyBatis and before he worked for this company all of server saurce was MyBatise so I need to study new skill for server as front end developer. so I was reading the old coworker's code I totally didn't understand those codes because the result type was just object array! so I needed to refectory those unreadable codes with JPA Projection

There are more ways for Projection but I wrote down what I tried and why I use the way

1. as POJO ->
```@Query(value = "SELECT new 경로.blablaDto(blaCol, blaCol2) from blaTable")```<br />
as the code, I needed to write but I need to get only 5 rows. It's impossble in JPQL<br />
2. as interface -> make get functions for mapping JPA result and alias every columns what has over 2 words to camel case like the get function what I made
```
public interface NewAuctionItem {
    String getName();
    ...
}

List<NewAuctionItem> find5NewBids();

```

Lastly, I chose second way.

**old code**
```
    List<Object[]> auction5 = auctionInfoRepository.find5New();
    ArrayList<AuctionItemDto> newAuctionItems = new ArrayList();
    for(int i=0; i<auction5.size(); i++){
      AuctionItemDto newAuctionItem = new AuctionItemDto();
      Object[] row = auction5.get(i);
      newAuctionItem.setName(String.valueOf(row[1]) + " " + String.valueOf(row[2]) + " " + row[9].toString());
      newAuctionItem.setMinBid(Long.valueOf(row[3].toString()));
      newAuctionItem.setNameImage(String.valueOf(row[4]));
      newAuctionItem.setImage(row[5].toString());
      newAuctionItem.setGoodsAuctionIdx(Long.valueOf(row[6].toString()));
      newAuctionItem.setStartDt(String.valueOf(row[7]));
      newAuctionItem.setFinishDt(String.valueOf(row[8]));
      newAuctionItem.setSpecialGift(Integer.parseInt(row[10].toString()));
      newAuctionItem.setWhiteName(row[11].toString());
      newAuctionItems.add(newAuctionItem);
    }
    mainDto.setNewAuctionItems(newAuctionItems);
```

**new code**

```
mainDto.setNewAuctions(auctionInfoRepository.find5NewBids());
```

I just changed return type This code is so easy to read right now and It's not duplicated anymore