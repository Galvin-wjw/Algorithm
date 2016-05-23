__author__ = 'galvin'
#-*-coding:utf-8-*-
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

    def reverse(self,head):
        prev = None     #最后一个为空
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
