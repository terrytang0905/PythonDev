package com.ttsoftware.utilities.algorithm.datastructure.ReaderFiles.Chap05.linkQueue;

// linkQueue.java
// demonstrates queue implemented as double-ended list
// to run this program: C>java LinkQueueApp
////////////////////////////////////////////////////////////////
class Link
   {
   public long dData;                // data item
   public Link next;                 // next link in list
// -------------------------------------------------------------
   public Link(long d)               // constructor
      { dData = d; }
// -------------------------------------------------------------
   public void displayLink()         // display this link
      { System.out.print(dData + " "); }
// -------------------------------------------------------------
   }  // end class Link
////////////////////////////////////////////////////////////////
class FirstLastList
   {
   private Link first;               // ref to first item
   private Link last;                // ref to last item
// -------------------------------------------------------------
   public FirstLastList()            // constructor
      {
      first = null;                  // no items on list yet
      last = null;
      }
// -------------------------------------------------------------
   public boolean isEmpty()          // true if no links
      { return first==null; }
// -------------------------------------------------------------
   public void insertLast(long dd) // insert at end of list
      {
      Link newLink = new Link(dd);   // make new link
      if( isEmpty() )                // if empty list,
         first = newLink;            // first --> newLink
      else
         last.next = newLink;        // old last --> newLink
      last = newLink;                // newLink <-- last
      }
   
// -------------------------------------------------------------
   public long deleteFirst()         // delete first link
      {                              // (assumes non-empty list)
      long temp = first.dData;
      if(first.next == null)         // if only one item
         last = null;                // null <-- last
      first = first.next;            // first --> old next
      return temp;
      }
// -------------------------------------------------------------
   public void displayList()
      {
      Link current = first;          // start at beginning
      while(current != null)         // until end of list,
         {
         current.displayLink();      // print data
         current = current.next;     // move to next link
         }
      System.out.println("");
      }
// -------------------------------------------------------------
   }  // end class FirstLastList
////////////////////////////////////////////////////////////////
class LinkQueue
   {
   private FirstLastList theList;
//--------------------------------------------------------------
   public LinkQueue()                // constructor
      { theList = new FirstLastList(); }  // make a 2-ended list
//--------------------------------------------------------------
   public boolean isEmpty()          // true if queue is empty
      { return theList.isEmpty(); }
//--------------------------------------------------------------
   public void insert(long j)        // insert, rear of queue
      { theList.insertLast(j); }
//--------------------------------------------------------------
   public long remove()              // remove, front of queue
      {  return theList.deleteFirst();  }
//--------------------------------------------------------------
   public void displayQueue()
      {
      System.out.print("Queue (front-->rear): ");
      theList.displayList();
      }
//--------------------------------------------------------------
   }  // end class LinkQueue
////////////////////////////////////////////////////////////////
class LinkQueueApp
   {
   public static void main(String[] args)
      {
      LinkQueue theQueue = new LinkQueue();
      theQueue.insert(20);                 // insert items
      //First time,the link first and link last point to the same memory address.
      theQueue.insert(40);
      //Second time,the link first and link last still point to the same memory address even if inserting the child ref into the link last.
      //Update the child next ref of link last is consistent with the link first.
      //The child next ref of link first is equal to the link last.
      //But the link last will be changed independently if new object is assigned to the link last. The link first is different from link last.

      theQueue.displayQueue();             // display queue

      theQueue.insert(60);                 // insert items
      theQueue.insert(80);

      theQueue.displayQueue();             // display queue

      theQueue.remove();                   // remove items
      theQueue.remove();

      theQueue.displayQueue();             // display queue
      }  // end main()
   }  // end class LinkQueueApp
////////////////////////////////////////////////////////////////
