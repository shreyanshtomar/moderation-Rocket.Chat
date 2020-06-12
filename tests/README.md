# How to run the Python tests

In the command line from the project working folder ```./moderation``` execute the following command:

```
python -m unittest discover -s tests -p '*_test.py' -v
```

Sample output:
```
test_sfw_image (inference_test.BasicTestCase) ... ok
test_sfw_image_sent_as_base64 (inference_test.BasicTestCase) ... FAIL

======================================================================
FAIL: test_sfw_image_sent_as_base64 (inference_test.BasicTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "D:\DevOps\GSoC\moderation\tests\inference_test.py", line 21, in test_sfw_image_sent_as_base64
    self.assertEqual(resp.status_code, 200)
AssertionError: 400 != 200

----------------------------------------------------------------------
Ran 2 tests in 0.401s

FAILED (failures=1)
```