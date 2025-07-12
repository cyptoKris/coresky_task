import requests
import threading
import time
import random
from eth_account import Account
from eth_account.messages import encode_defunct
from loguru import logger


class Project:
    def __init__(self, table_info):
        self.table_info = table_info
        self.session = requests.Session()
        
    def checksum_address(self, address):
        """Convert address to checksum format"""
        return Account.to_checksum_address(address)
    
    def okx_sign_message(self, message, private_key):
        """Sign message using private key"""
        account = Account.from_key(private_key)
        message_hash = encode_defunct(text=message)
        signature = account.sign_message(message_hash)
        return signature.signature.hex()
    
    def action(self):
        """Base action method to be overridden by subclasses"""
        pass


def thead_run_task(group_lists, task_class, no_act):
    """Run tasks in threads for each group"""
    for group_list in group_lists:
        for obj in group_list:
            try:
                task = task_class(obj)
                task.action()
                logger.success(f"浏览器{obj.browser_number} 任务完成")
            except Exception as e:
                logger.error(f"浏览器{obj.browser_number} 任务失败: {str(e)}")
                no_act.add(obj.browser_number)
            time.sleep(random.uniform(1, 3))