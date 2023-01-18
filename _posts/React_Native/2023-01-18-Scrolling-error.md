# 오늘의 에러 - 안드로이드에서 스크롤 버벅거리는 에러

`플랫폼 - React Native + Expo`

> 애플과 구형폰에서는 정상적으로 스크롤링이 됐지만, `신형 안드로이드에서는 스크롤링을 하면 버벅거리는 현상`이 있었다.
> 페이지 구조는 부모 스크롤 아래 다양한 자식 컴포넌트가 존재했고 그중에서 고화질의 사진 여러장이 있었다.

코드 소스는 간단하게 아래와 같다.

```
<ScrollView>
	<ScrollView>
		<Image /> //8장의 이미지
		...
	</ScrollView>
	<View>
		<Image /> //8장의 이미지
	</View>	
</ScrollView>
```

이 에러는 결국 화면 주사율 때문이라고 추축이 되지만 정확한건 많은 양의 고화질 이미지가 스크롤에 있는 바람에 발생하는 에러이며, 이부분은 removeClippedSubviews={true} 속성 값을 부모 ScrollView에 추가해서 해결 했다.

```
<ScrollView
	removeClippedSubviews={true}>
	<ScrollView>
		<Image /> //8장의 이미지
		...
	</ScrollView>
	<View>
		<Image /> //8장의 이미지
	</View>	
</ScrollView>
```

이렇게 하면 FlatList와 같이 화면에 보이는 부분만 렌더링을 하며, 나머지 부분은 overflow:hidden과 같은 효과를 보인다.