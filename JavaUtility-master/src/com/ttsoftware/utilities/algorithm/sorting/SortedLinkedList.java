package com.ttsoftware.utilities.algorithm.sorting;

import java.util.*;

public class SortedLinkedList<E extends Comparable<? super E>> extends LinkedList<E>
{
    /**
	 * 
	 */
	private static final long serialVersionUID = -5765910495513984558L;

	@SuppressWarnings("unchecked")
	public void mergeLists(SortedLinkedList<E> list1, SortedLinkedList<E> list2)
    {
        ListIterator<E> itr1 = list1.listIterator(); //List Iterator for the first list
        ListIterator<E> itr2 = list2.listIterator(); //List Iterator for the second list
        
        while(itr1.hasNext() || itr2.hasNext())
        {
            E item1 = null; //variable to first node in first list
            E item2 = null; //variable to first node in second list
            
            if(itr1.hasNext())
            {
                item1 = itr1.next();
            }
            if(itr2.hasNext())
            {
                item2 = itr2.next();
            }
            if(item1 == null)
            {
                while(list2 != null)
                {
                    item1 = itr2.next();
                }
            }
            else if(item2 == null)
            {
                while(list1 != null)
                {
                    item2 = itr1.next();
                }
            }
            else if(item1.compareTo(item2) < 0)
            {
                addLast(item1);
                itr1.remove();             
            }
            else
            {
                addLast(item2);
                itr2.remove();
            }
        }
            
            
    }
}
