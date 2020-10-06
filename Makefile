.PHONEY: lint format diff deploy destroy

lint:
	flake8 .
	isort --check-only --profile black .
	black --check --diff .

format:
	isort --profile black .
	black .

diff:
	cdktf diff || true

deploy:
	cdktf deploy --auto-approve true

destroy:
	cdktf destroy --auto-approve true
