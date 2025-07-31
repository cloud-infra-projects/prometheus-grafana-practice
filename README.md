# FastAPI + Prometheus + Grafana 모니터링 실습

## 실습 목표

FastAPI 애플리케이션을 Prometheus 및 Grafana로 모니터링

## 구성 요소

- FastAPI (Uvicorn)
- Prometheus
- Grafana
- Docker Compose

## 주요 실습 단계

1. FastAPI 애플리케이션 생성
2. 메트릭 엔드포인트 `/metrics` 구현
3. Prometheus 구성 및 `/metrics` 스크레이핑 설정
4. FastAPI 요청 트래픽 수집
5. Prometheus에서 시계열 데이터 확인
6. Grafana를 통해 대시보드 시각화
