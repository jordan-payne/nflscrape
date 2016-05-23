init:
	pip install -r requirements.txt
clean:
	-rm -f -v */*.pyc
	-rm -rf **/.cache
	-rm -rf **/__pycache__
	-rm -f -v **/ghostdriver.log
	-rm -rf tests/docs
test: pytest clean

pytest:
ifeq ($(runslow),true)
	-py.test --runslow --username=$(username) --password=$(password)
else
	-py.test --username=$(username) --password=$(password)
endif
	killall phantomjs
