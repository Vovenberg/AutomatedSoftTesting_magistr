#!/usr/bin/env bash
cd ../pr2/
nosetests --with-coverage app_calculate_test.py
nosetests --rednose
py.test app_calculate_test.py
py.test --cov app_calculate.py
