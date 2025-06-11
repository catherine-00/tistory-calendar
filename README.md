# tistory-calendar 업데이트 방법



## 1. `rss_parser.py` 실행
```bash
python rss_parser.py
```

=> `tistory_post_counts.json` 만들어짐


## 2. `tistory_post_counts.json` git push 하기
- 이러면 티스토리 사이드바 업데이트됨

## 티스토리에 iframe 형식으로 삽입하는 코드
```html
<iframe 
  src="깃허브의 calendar.html 주소" 
  width="100%" 
  height="600"       <!-- ✅ 추천: 270~300px 사이 -->
  style="border: none;"
></iframe>

```

