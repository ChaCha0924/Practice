{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "be834c41-614d-46bc-9fb0-d60fd8494666",
   "metadata": {},
   "source": [
    "## 프로그래밍이란?\n",
    "    - 프로그래밍 언어를 사용하여 프로그램을 개발하는 것\n",
    "    - 논리적인 사고를 가질 수 있다.\n",
    "## programing language?\n",
    "    - 프로그램을 개발할 때 사용하는 도구\n",
    "    - 인간이 원하는 것을 컴퓨터에게 명령할 때 사용하는 컴퓨터가 이해할 수 있는 언어\n",
    "    \n",
    "## 파이썬?\n",
    "    - 쉽다. 간결하다.\n",
    "    - 라이브러리가 많다.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "429780a3-ca42-482e-8e08-ed4c6a45d071",
   "metadata": {},
   "source": [
    "## Chapter 2. Data: Types, Values, Variables, and Names"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ef50cd32-87c1-43e0-83f3-40aa9e90e3f5",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = 2\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0646837f-01ac-4ef4-ba4a-72bdda896496",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a == 2"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ba3d2c1c-7112-455d-9906-50d002f3c0df",
   "metadata": {},
   "source": [
    "- 변수|variable: 특정 값을 저장하는 공간\n",
    "    a\n",
    "- 값|value\n",
    "    2\n",
    "- 할당하다|assign: 변수에 값을 넣는 과정\n",
    "    \"2를 a에 넣었다.\"\n",
    "    \n",
    "    *** a는 2다. a == 2\n",
    "- 자료형|type: 데이터의 형태\n",
    "    a 데이터의 형태? integer (int 타입이다)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d58f827d-e265-4565-8fd4-59c812cdbadb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "dc728f56-5a53-4234-ac38-6e744d86484b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "44ed2fff-41c9-410f-aaae-44f0fb22843b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# type\n",
    "type(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "74dce7a8-77c5-4cc6-bab0-c09c31cf6ad4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "64488d2c-f93f-44b9-b9b0-9efc98edb21d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "bool"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(a == 2) # bool, boolean T/F"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4967d833-a205-4fdd-8676-ca8ac4e3ebdf",
   "metadata": {},
   "source": [
    "### Type\n",
    "-integer|정수 : 1, 2, 3, .. (int)\n",
    "-floating point number|부동소수점: 1.0, 2.0, ..., 0.4 (float)\n",
    "-string|문자열: \"1\", 'apple' (str)\n",
    "-boolean|불리언: True/False (bool)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "8e962ae7-20a9-471b-9c15-9b6361e591ac",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(\"1\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "9a0242b0-9bdc-4f37-85fb-d4eeccda0372",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type('apple')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "27f36620-9ea6-4ac9-9c52-9e0b9ac8d4b4",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'apple' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_2568/2423857472.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mtype\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mapple\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;31m#변수명\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'apple' is not defined"
     ]
    }
   ],
   "source": [
    "type(apple) #변수명"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "efbc95ed-ee5a-4eaa-87d2-b8f02951d87f",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "name = 'kim'\n",
    "name\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "da6c0fa3-c063-42ab-bc6f-d051597e5add",
   "metadata": {},
   "source": [
    "### "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
