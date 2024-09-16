class Functions:
    
    def __init__(self):     
        pass
    

    def get_cost(self, lst_of_all_items, cost_of_all_items, list_of_items_in_busket) -> int:
        """
        Args:
            lst_of_all_items (list): list of all items
            cost_of_all_items (list): cost of all items 

        Returns:
            int: _description_
        """        
        
        cost = 0
        
        for item in list_of_items_in_busket:
            for items in lst_of_all_items:
                if items == item:
                    cost = cost + cost_of_all_items[lst_of_all_items.index(items)]
                                    
        return cost

    
    def get_pay_check(self, cost, lst_of_items) -> str:
        
        """
        Args:
            cost (int): cost of all items in busket
            lst_of_items (list): list of items in busket

        Returns:
            str: text of check
        """        
        
        text = ''
        text = text + 'В ваш заказ входит:\n'
        for i in range(len(lst_of_items)):
            text = text + str(lst_of_items[i]) + '\n'
        
        text = text + 'Стоимость заказа: ' + str(cost) + ' рублей'
        
        return text