from multiping import MultiPing

def ping(host,n):
    avg=0
    ret_value_list=[]
    pass_fail_list=[]
    for i in range (n):
        ret_value=sub(host)
        
        if ret_value==0.0:
            pass_fail_list.append('Fail')
        else:
            pass_fail_list.append('Pass')
            
            
        #print('Return value for Number {} ping is {}'.format(i,ret_value))
        ret_value_list.append(ret_value)
        
        
    else:
        avg=sum(ret_value_list)/n
        print( "{} '\n'{}".format(pass_fail_list,ret_value_list))
        print('Average Return value for {} ping is {}'.format(n,avg))
        
def sub(host):
        RTT = ''
        mp = MultiPing([host])
        mp.send()

            # With a 1 second timout, wait for responses (may return sooner if all
            # results are received).
        responses, no_responses = mp.receive(1)
        for addr, rtt in responses.items():
            RTT = rtt

        return RTT
'''

        if no_responses:
                # Sending pings once more, but just to those addresses that have not
                # responded, yet.
            mp.send()
            responses, no_responses = mp.receive(1)
            RTT = -1
       

'''
#Getting the latency average (in seconds) of host '192.168.79.7' using 10 samples
ping('192.168.79.7',10)
