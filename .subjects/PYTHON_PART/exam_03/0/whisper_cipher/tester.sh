#!/bin/bash

index=0
if [ -e traceback ]; then rm traceback; fi

cd .system/grading

cat > _test_ref.py << 'PYEOF'
import importlib.util, sys

spec = importlib.util.spec_from_file_location("ref", "whisper_cipher.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
f = mod.whisper_cipher

tests = [
    ("Hello, World!", 3),
    ("Abz", 3),
    ("WXYZ 1", 1),
    ("abc", 0),
    ("xyz", 2),
    ("", 5),
    ("Hello, World!", 0),
]
for args in tests:
    print(f(*args))
PYEOF

python3 _test_ref.py > _source_out 2>&1

cat > _test_student.py << 'PYEOF'
import importlib.util, sys

spec = importlib.util.spec_from_file_location("student", "../../rendu/whisper_cipher/whisper_cipher.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
f = mod.whisper_cipher

tests = [
    ("Hello, World!", 3),
    ("Abz", 3),
    ("WXYZ 1", 1),
    ("abc", 0),
    ("xyz", 2),
    ("", 5),
    ("Hello, World!", 0),
]
for args in tests:
    print(f(*args))
PYEOF

python3 _test_student.py > _student_out 2>&1

DIFF=$(diff _source_out _student_out)

if [ "$DIFF" = "" ]; then
    touch passed
else
    index=1
    echo "Tests FAILED:" >> traceback
    echo "" >> traceback
    echo "Expected output:" >> traceback
    cat _source_out >> traceback
    echo "" >> traceback
    echo "Your output:" >> traceback
    cat _student_out >> traceback
fi

rm -f _test_ref.py _test_student.py _source_out _student_out
{ mv traceback ../../traceback; } 2>/dev/null || true
cd ../..
