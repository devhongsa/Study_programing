from sqlalchemy import create_engine, MetaData, Table

# Redshift 연결 정보 설정
db_username = "admin"
db_password = "Qwer1234!"
db_host = "default.364472264080.us-west-2.redshift-serverless.amazonaws.com"
db_port = 5439
db_name = "dev"

# SQLAlchemy 엔진 생성
engine = create_engine(f"postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}")

# 연결 테스트
try:
    connection = engine.connect()
    print("Redshift에 성공적으로 연결되었습니다.")
    
    query = "select * from raw_data.apartment_sale_info limit 10"
    
    result = connection.execute(query)
    
    # 결과 처리
    for row in result:
        print(row)
        
    connection.close()
except Exception as e:
    print("연결 실패:", str(e))