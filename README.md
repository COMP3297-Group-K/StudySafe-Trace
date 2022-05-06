# StudySafe-Trace User Guide

| Description     | URL                                                 |
| --------------- | --------------------------------------------------- |
| StudySafe Trace | http://group-k-studysafe-trace.herokuapp.com/trace/ |

| Repository and project root                                  | Configuration root     | App root              |
| ------------------------------------------------------------ | ---------------------- | --------------------- |
| [StudySafe-Trace](https://github.com/COMP3297-Group-K/StudySafe-Trace) | StudySafe-Trace/config | StudySafe-Trace/trace |

### StudySafe Trace Example Usage

- View the full list of infected HKU members: http://group-k-studysafe-trace.herokuapp.com/trace

 - View the full list of close contacts: http://group-k-studysafe-trace.herokuapp.com/trace/contacts

 - View the full list of venues visited by the infectious two days before onset/diagnosis: http://group-k-studysafe-trace.herokuapp.com/trace/venues

 - View `hkuID`'s close contacts: [http://group-k-studysafe-trace.herokuapp.com/trace/contacts/<hkuID\>]() 

   e.g. http://group-k-studysafe-trace.herokuapp.com/trace/contacts/3025704501

 - View the venues visited by `hkuID` two days before onset/diagnosis: [http://group-k-studysafe-trace.herokuapp.com/trace/venues/<hkuID\>]() 

   e.g. http://group-k-studysafe-trace.herokuapp.com/trace/venues/3025704501

   - If you input the incorrect `hkuID` (i.e., the one not on the list of the infected people), the page will generate an error. 

**Note: **In the demo, we use hku id `3025704501`, `3025258327`, `3023776542` for simple demonstration. 



