package com.ttsoftware.utilities.algorithm.sorting;

public class SelectionSort {
	//n*n
	public static void selectionSort(int[] elements){
        for(int i = 0; i < elements.length-1; ++i){
            int k = i;
            for(int j = i; j < elements.length; ++j){
                if(elements[k] > elements[j]){
                    k = j;
                }
            }
            if(k != i){//交换元素
                int temp = elements[i];
                elements[i] = elements[k];
                elements[k] = temp;
            }
        }
}
}
