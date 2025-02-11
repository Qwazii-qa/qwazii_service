# QWAZII Service

* 자동화 테스트 강의용 Sample 서비스

## Login User Info
```bash
id : qwazii
pw : test111222
token : 3a8f3044ff3c12a196ef7ec35f8290d395be6e90
```


## UI
### Login page

#### 주요 요소
- Username 입력 필드
- Password 입력 필드
- "아이디 저장" 체크박스
- 로그인 버튼

#### 기능
- 로그인 성공 시 상품 목록으로 이동
- 로그인 실패 시 에러 메시지 표시
- "아이디 저장" 선택 시 브라우저에 저장

### Logout page

#### 주요 요소
- 로그아웃 완료 메시지
- "다시 로그인" 버튼

#### 기능
- 세션 종료 및 쿠키 삭제
- 로그인 페이지로 이동 링크 제공

### Product List

#### 주요 요소
- 상품 목록 테이블
  - 상품명
  - 카테고리
  - 단가
  - 판매가격
  - 제조사
  - 재고 수량
  - 수수료
  - 관리 버튼(수정/삭제)
- "새 상품 등록" 버튼

#### 네비게이션
- 상품 목록
- API
- 로그아웃

### Product 등록/수정

#### 주요 요소
- 입력 폼
  - 상품명 입력 필드
  - 카테고리 선택 드롭다운
  - 단가 입력 필드
  - 판매가격 입력 필드
  - 제조사 입력 필드
  - 재고 수량 입력 필드
  - 수수료 입력 필드
- 저장 버튼
- 취소 버튼

### Product 삭제

#### 주요 요소
- 삭제 확인 메시지
- 삭제 버튼
- 취소 버튼

## API

### API 인증

API를 사용하기 위해서는 Token 인증이 필요합니다.

#### 인증 헤더
모든 API 요청에 다음 헤더를 포함해야 합니다:
```
Authorization: Token 3a8f3044ff3c12a196ef7ec35f8290d395be6e90
```

### GET /api/products

전체 상품 목록을 조회합니다.

#### 요청
```bash
curl -H "Authorization: Token 3a8f3044ff3c12a196ef7ec35f8290d395be6e90" \
     http://localhost:8000/api/products/
```

#### 응답
```json
[
    {
        "id": 1,
        "name": "Example Product",
        "category": 1,
        "cost_price": "100.00",
        "selling_price": "150.00",
        "manufacturer": "Example Corp",
        "stock_quantity": 10,
        "commission_rate": "5.00",
        "created_at": "2025-02-11T10:00:00Z",
        "updated_at": "2025-02-11T10:00:00Z"
    }
]
```

### GET /api/products/1

특정 상품의 상세 정보를 조회합니다.

#### 요청
```bash
curl -H "Authorization: Token 3a8f3044ff3c12a196ef7ec35f8290d395be6e90" \
     http://localhost:8000/api/products/1/
```

#### 응답
```json
{
    "id": 1,
    "name": "Example Product",
    "category": 1,
    "cost_price": "100.00",
    "selling_price": "150.00",
    "manufacturer": "Example Corp",
    "stock_quantity": 10,
    "commission_rate": "5.00",
    "created_at": "2025-02-11T10:00:00Z",
    "updated_at": "2025-02-11T10:00:00Z"
}
```

### POST /api/products

새로운 상품을 등록합니다.

#### 요청
```bash
curl -X POST \
     -H "Authorization: Token 3a8f3044ff3c12a196ef7ec35f8290d395be6e90" \
     -H "Content-Type: application/json" \
     -d '{
         "name": "New Product",
         "category": 1,
         "cost_price": "100.00",
         "selling_price": "150.00",
         "manufacturer": "Test Corp",
         "stock_quantity": 10,
         "commission_rate": "5.00"
     }' \
     http://localhost:8000/api/products/
```

#### 필수 필드
- name: 상품명 (문자열)
- category: 카테고리 ID (정수)
- cost_price: 단가 (decimal)
- selling_price: 판매가격 (decimal)
- manufacturer: 제조사 (문자열)
- stock_quantity: 재고 수량 (정수)
- commission_rate: 수수료율 (decimal)

#### 응답
```json
{
    "id": 2,
    "name": "New Product",
    "category": 1,
    "cost_price": "100.00",
    "selling_price": "150.00",
    "manufacturer": "Test Corp",
    "stock_quantity": 10,
    "commission_rate": "5.00",
    "created_at": "2025-02-11T10:30:00Z",
    "updated_at": "2025-02-11T10:30:00Z"
}
```

### PUT /api/products/1

기존 상품의 정보를 전체 수정합니다.

#### 요청
```bash
curl -X PUT \
     -H "Authorization: Token 3a8f3044ff3c12a196ef7ec35f8290d395be6e90" \
     -H "Content-Type: application/json" \
     -d '{
         "name": "Updated Product",
         "category": 1,
         "cost_price": "120.00",
         "selling_price": "180.00",
         "manufacturer": "Test Corp",
         "stock_quantity": 15,
         "commission_rate": "5.00"
     }' \
     http://localhost:8000/api/products/1/
```

#### 필수 필드
PUT 요청 시에는 모든 필드가 필수입니다. (POST 요청과 동일)

#### 응답
```json
{
    "id": 1,
    "name": "Updated Product",
    "category": 1,
    "cost_price": "120.00",
    "selling_price": "180.00",
    "manufacturer": "Test Corp",
    "stock_quantity": 15,
    "commission_rate": "5.00",
    "created_at": "2025-02-11T10:00:00Z",
    "updated_at": "2025-02-11T11:00:00Z"
}
```

### DELETE /api/products/1

특정 상품을 삭제합니다.

#### 요청
```bash
curl -X DELETE \
     -H "Authorization: Token 3a8f3044ff3c12a196ef7ec35f8290d395be6e90" \
     http://localhost:8000/api/products/1/
```

#### 응답
성공 시 204 No Content 응답을 반환합니다.

#### 에러 응답
모든 API 요청에 대해 다음과 같은 에러 응답이 발생할 수 있습니다:

- 401 Unauthorized: 인증 실패
```json
{
    "detail": "자격 인증데이터(authentication credentials)가 제공되지 않았습니다."
}
```

- 404 Not Found: 리소스를 찾을 수 없음
```json
{
    "detail": "찾을 수 없습니다."
}
```

- 400 Bad Request: 잘못된 요청
```json
{
    "field_name": [
        "에러 메시지"
    ]
}
```

@Qwazii
