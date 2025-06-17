# tistory-calendar 

## 티스토리 백업 파일에서 날짜 읽어오기
1. post_date.ipynb 실행
2. backup_date.json 파일 생성


## 최신 포스팅 글 날짜 읽어오기(공개 글만)
1. `rss_parser.py` 실행
2. `tistory_post_counts.json` 만들어짐


## 백업 파일의 날짜와 최신 날짜 합치기
1. merge_posts.ipynb 실행
2. final_date.json 생성

## 2. `final_date.json` git push 하기
- 이러면 티스토리 사이드바 업데이트됨


## 티스토리에 iframe 형식으로 삽입하는 코드
```html
<iframe 
  src=" https://catherine-00.github.io/tistory-calendar/calendar.html" 
  width="100%" 
  height="350"       <!-- ✅ 추천: 270~300px 사이 -->
  style="border: none;"
></iframe>

```


tistory_posts/
├── posts.json           ← 이 파일이 계속 누적·관리됨
├── parse_backup.py      ← 백업에서 추출
├── parse_rss.py         ← RSS에서 추출
├── merge_posts.py       ← json 병합 및 중복 제거
├── backup.xml           ← 티스토리 백업 파일
├── rss.json             ← 최신 rss 파싱 결과
