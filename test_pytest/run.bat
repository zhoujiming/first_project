:: -*- coding: utf-8 -*-
:: Date: 2020/9/18

:: 生成xml格式的报告
pytest -v test_1.py --junitxml=./report/test_1.xml
pytest -v test_2.py --junitxml=./report/test_2.xml

:: 生成txt格式的报告
pytest -v test_1.py --resultlog=./report/test_1.log
pytest -v test_2.py --resultlog=./report/test_2.log

:: 生成html格式的报告
pytest -v test_1.py --html=./report/test_1.html
pytest -v test_2.py --html=./report/test_2.html