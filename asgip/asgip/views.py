from django.http import HttpResponse
import datetime,asyncio,time
from asgiref.sync import sync_to_async

def sync_view(request):
    start_time = datetime.datetime.now()
    print(datetime.datetime.now())
    task1 = hello_1()
    task2 = hello_2()
    task3 = hello_3()
    task4 = hello_4()
    print(task1,task2,task3,task4)
    total = datetime.datetime.now() - start_time
    print("total:",total)
    return  HttpResponse(datetime.datetime.now())

def hello_1():
    print('synchello1')
    time.sleep(2)
    print('wakeup')
    sync_list  =[i for i in range(1,101,2)]     
    return sync_list

def hello_2():
    print('synchello2')
    time.sleep(2)
    print('wakeup')
    sync_list  =[i for i in range(1,101,2)]     
    return sync_list

def hello_3():
    print('synchello3')
    time.sleep(2)
    print('wakeup')
    sync_list  =[i for i in range(1,101,2)]     
    return sync_list

def hello_4():
    print('synchello4')
    time.sleep(2)
    print('wakeup')
    sync_list  =[i for i in range(1,101,2)]     
    return sync_list



async def index(request):
    start_time = datetime.datetime.now()
    print(datetime.datetime.now())
    task1 = asyncio.ensure_future(hello1())
    task2 = asyncio.ensure_future(hello2())
    task3 = asyncio.ensure_future(hello3())
    task4 = asyncio.ensure_future(hello4())
    print(task1,task2,task3,task4)
    await asyncio.wait([task1,task2,task3,task4])
    total = datetime.datetime.now() - start_time
    print('total',total)
    return  HttpResponse(datetime.datetime.now())


@sync_to_async 
def hello1():
    print('asynchello1')
    async_list  =[i for i in range(1,101,2)] 
    time.sleep(2)
    print('wakeup')
    return async_list

@sync_to_async 
def hello2():
    print('asynchello2')
    async_list  =[i for i in range(1,101,2)]  
    time.sleep(2)
    print('wakeup')
    return async_list

@sync_to_async 
def hello3():
    print('asynchello3')
    async_list  =[i for i in range(1,101,2)]
    time.sleep(2)
    print('wakeup')
    return async_list

@sync_to_async 
def hello4():
    print('asynchello4')  
    async_list =[i for i in range(1,101,2)]
    time.sleep(2)
    print('wakeup')
    return async_list