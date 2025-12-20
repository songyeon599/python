# 행렬을 사용자로부터 입력받는 함수
def input_matrix(name):
    print(f"\n{name} 행렬을 입력하세요.")

    # 행렬의 행(row)과 열(column) 개수 입력 받기
    rows = int(input(f"{name}의 행(row) 개수: "))
    cols = int(input(f"{name}의 열(column) 개수: "))

    matrix = []  # 빈 행렬 리스트 생성

    print(f"{name}의 각 행을 공백으로 구분해 입력하세요 (예: 1 2 3):")
    for i in range(rows):
        # 한 줄 입력받고 숫자 리스트로 변환
        row = list(map(int, input(f"{i+1}번째 행: ").split()))

        # 입력된 열 개수가 일치하지 않으면 다시 입력받기
        if len(row) != cols:
            print("❌ 열의 개수가 일치하지 않습니다. 다시 입력하세요.")
            return input_matrix(name)  # 재귀 호출로 다시 입력받음

        matrix.append(row)  # 유효한 행이면 행렬에 추가

    return matrix  # 완성된 행렬 반환


# 행렬을 예쁘게 출력해주는 함수
def print_matrix(matrix, title):
    print(f"\n🔢 {title}:")
    for row in matrix:
        print("  ", row)


# 행렬 덧셈 함수: 두 행렬 A, B의 같은 위치에 있는 원소끼리 더함
def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


# 행렬 뺄셈 함수: 두 행렬 A, B의 같은 위치에 있는 원소끼리 뺌
def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


# 행렬 곱셈 함수: A × B를 수식으로 구현
def multiply_matrices(A, B):
    result = []  # 결과 행렬을 저장할 리스트

    # A의 각 행마다 반복
    for i in range(len(A)):
        row = []  # 결과 행의 한 줄을 저장할 리스트

        # B의 각 열마다 반복
        for j in range(len(B[0])):
            sum_product = 0  # 행×열 곱의 합

            # A의 행의 원소와 B의 열의 원소를 곱해서 모두 더함
            for k in range(len(A[0])):  # A의 열 개수 == B의 행 개수
                sum_product += A[i][k] * B[k][j]

            row.append(sum_product)  # 계산된 값을 결과 행에 추가

        result.append(row)  # 결과 행을 결과 행렬에 추가

    return result  # 최종 곱셈 결과 반환


# 프로그램의 메인 실행 함수
def main():
    print("🧮 순수 파이썬 행렬 계산기")

    # 사용자로부터 두 개의 행렬 입력받기
    A = input_matrix("A")
    B = input_matrix("B")

    # 입력된 행렬 출력
    print_matrix(A, "A 행렬")
    print_matrix(B, "B 행렬")

    # 덧셈/뺄셈: 두 행렬의 크기가 같아야 함
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        print_matrix(add_matrices(A, B), "A + B")     # 덧셈 결과 출력
        print_matrix(subtract_matrices(A, B), "A - B")  # 뺄셈 결과 출력
    else:
        print("\n❌ 덧셈/뺄셈 불가능: 두 행렬의 크기가 다릅니다.")

    # 곱셈: A의 열 개수 == B의 행 개수여야 곱셈 가능
    if len(A[0]) == len(B):
        print_matrix(multiply_matrices(A, B), "A × B")  # 곱셈 결과 출력
    else:
        print("\n❌ 곱셈 불가능: A의 열 개수와 B의 행 개수가 달라요.")


# 프로그램이 직접 실행될 경우 main() 호출
if __name__ == "__main__":
    main()
