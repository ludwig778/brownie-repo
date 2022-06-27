
compile:
	poetry run brownie compile

tests:
	poetry run brownie test
.PHONY: tests

clean:
	rm -rf build/deployments/5777 build/deployments/5778
