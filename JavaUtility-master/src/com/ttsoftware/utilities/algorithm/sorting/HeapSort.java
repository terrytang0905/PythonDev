package com.ttsoftware.utilities.algorithm.sorting;

public class HeapSort {
	
	int elements[];
	
	public static void main(String[] args){
		int data[]={11,43,1,31,15,99};
		HeapSort hsort=new HeapSort();
		hsort.heapSort(data);
	}
	

	public void heapSort(int[] elements) {
		this.elements=elements;
		for (int i = elements.length - 1; i > 0; i--) {
			buildHeap(elements, i);// 建堆
			swap(elements, 0, i);// 交换根节点和最后一个节点
		}
		display();
	}

	private void buildHeap(int[] elements, int lastIndex) {
		int lastParentIndex = (lastIndex - 1) / 2;// 获得最后一个父节点
		for (int i = lastParentIndex; i >= 0; i--) {
			int parent = elements[i];
			int leftChild = elements[i * 2 + 1];// 左节点肯定存在
			int rightChild = leftChild;
			if (i * 2 + 2 <= lastIndex) {
				rightChild = elements[i * 2 + 2];// 右节点不一定存在
			}
			int maxIndex = leftChild < rightChild ? i * 2 + 2 : i * 2 + 1;
			if (parent < elements[maxIndex]) {
				swap(elements, i, maxIndex);
			}
		}
	}

	private void swap(int[] elements, int firstIndex, int secondIndex) {
		int temp = elements[firstIndex];
		elements[firstIndex] = elements[secondIndex];
		elements[secondIndex] = temp;
	}
	
	public void display()
	{
		for(int i=0;i<elements.length;i++)
		{
			System.out.print(elements[i]);
			System.out.print(" ");
		}
		System.out.println(";");
	}
}
