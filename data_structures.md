# 시나리오별 선택 자료구조 및 근거

### 1. 상품코드를 입력하면 즉시 재고 수량을 확인해야 하는 재고 관리 데이터
* **1 선택한 자료구조:** Dictionary
* **2 선택 근거:** key를 통해 value를 을 즉시 찾아야 하기 때문
* **3 예시 코드:**
    ```python
    inventory = {"ITEM001": 50, "ITEM002": 15, "ITEM003": 0}
    target_code = "ITEM001"
    stock = inventory.get(target_code, 0)
    print(f"{target_code}의 재고: {stock}개")
    ```

### 2. 이벤트 응모 고객 명단에서 중복 응모를 제거하고, 기존 회원 명단과의 교집합을 구하는 상황
* **1 선택한 자료구조:** Set
* **2 선택 근거:** 교집합 연산을 통해 중복을 제거하고, 포함 여부만을 확인하기 때문
* **3 예시 코드:**
    ```python
    event_applicants = {"user1", "user2", "user2", "user3"}
    existing_members = {"user2", "user3", "user4"}
    valid_winners = event_applicants & existing_members
    print(f"유효 응모자: {valid_winners}")
    ```

### 3. 월별 매출액을 1월부터 12월까지 순서대로 저장하고 순회하는 데이터
* **1 선택한 자료구조:** List
* **2 선택 근거:** 시간순, 월별 등 순서가 있는 목록을 저장해야하기 때문.
* **3 예시 코드:**
    ```python
    monthly_sales = [1200, 1500, 1300, 1800, 2000, 2100, 1900, 2200, 2400, 2300, 2500, 2800]
    total_sales = sum(monthly_sales)
    for month, sales in enumerate(monthly_sales, start = 1):
        print(f"{month}월 매출: {sales:,}원")
    ```

### 4. 한 번 발급되면 절대 변경되어서는 안 되는 (위도, 경도) 매장 좌표
* **1 선택한 자료구조:** Tuple
* **2 선택 근거:** 한 번 정해지면 바뀌면 안 되는 데이터를 다루기 때문
* **3 예시 코드:**
    ```python
    store_location = (37.5509, 126.9410)
    latitude, longitude = store_location
    print(f"매장 위치 - 위도: {latitude}, 경도: {longitude}")
    ```

### 5. 1,000만 줄짜리 웹 서버 접속 로그 파일에서 특정 조건의 줄 수를 세는 작업
* **1 선택한 자료구조:** Generator
* **2 선택 근거:**
    - **자료구조 관점:** 1,000만 줄의 방대한 데이터를 List에 한 번에 담으면 Out of Memory 에러 발생함. Generator는 파일을 한 번에 다 읽어오지 않고, 호출될 때마다 한 줄씩 처리해 적은 메모리만 사용하여 안정적으로 처리할 수 있기 때문.
    - **처리 방식 관점:** 파일 전체를 미리 다 읽어오는 대신, `for line in f:`와 `yield`를 결합하여 한 줄을 읽어 조건에 맞는지 확인하고 반환한 뒤 대기하는 Lazy Evaluation 방식으로 동작하므로 시스템 과부하 없이 안정적으로 처리할 수 있음.
* **3 예시 코드:**
    ```python
    def count_error_logs(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                if "ERROR 404" in line:
                    yield 1
    ```