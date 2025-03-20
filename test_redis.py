import redis
import time

def test_redis_connection(max_retries=3, retry_delay=2):
    """
    Test Redis connection with retries
    
    Args:
        max_retries (int): Maximum number of connection attempts
        retry_delay (int): Delay between retries in seconds
    """
    for attempt in range(max_retries):
        try:
            print(f"\nAttempt {attempt + 1} of {max_retries}")
            
            # Create Redis client
            r = redis.Redis(
                host='localhost',
                port=6379,
                decode_responses=True,
                socket_timeout=5,
                retry_on_timeout=True
            )
            
            # Test connection with PING
            if r.ping():
                print("Redis PING successful!")
            
            # Test data operations
            r.set('test_key', 'test_value')
            value = r.get('test_key')
            
            print(f"Redis connection successful!")
            print(f"Test key-value operation successful: {value}")
            print(f"Redis info: {r.info('server')}")
            return True
            
        except redis.ConnectionError as e:
            print(f"Connection Error: {str(e)}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("Max retries reached. Redis connection failed.")
                return False
                
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return False

if __name__ == "__main__":
    test_redis_connection() 