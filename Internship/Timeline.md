---
tags:
  - Internship
---
a# 1st day
Installing project, dependencies, all software, framework required
# 2nd day
* .NET core framework
* Thêm service vào installer - service Installer 
## Model
* Is an object that represents the data (DB) in the application
## DTO
* Is an object that represents the data (DB) in the application but with more calculated characteristic 
## Controller
* Object that handles HTTP requests
## Installer
* Object to adding dependencies - to the API
## Helper
* self created add-ins
## DATA
* Data context
## Services
* The object where we 
## Task
create a new table in mySQL
* name Room
	* ID
	* BuidingID
	* RoomNum
	* RoomTypeID
	* CreateDate
	* CreateBy
	* Status
	* Room_Guid
### Step
* Model - Add model of the table as a new file
* DTO - Add DTO model of the table as a new file ( could be configured to fit user demand)
* Data - Dbset into BookingAppContext
* Service
* Installer
* Controllers - Mapper
# 3rd day
* _repo_ is the database
* Thêm campus với floor, campus floor, room, and building using GUID instead of ID
* Learn how to apply filter to ASP net Core for searching

# 4th day
* Create database - reading erd diagram
* Doing booking task
	1. model the booking db into the API system (5 steps adding)
	2. adding norm API set
	3. modify the adding(booking)(post) API to check if the room is available to book by checking
		1. CampusGuid
		2. BuildingGuid
		3. FloorGuid
		4. RoomGuid
		5. BookingDate
		6. if the time is conflict
	4. test the function
		1. testcase 1: conflict time in same day - check
		2. testcase 2: conflict time in another day - check
		3. testcase 3: conflict campus - check
		4. testcase 4: conflict building
		5. testcase 5: conflict floor
		6. testcase 6: conflict Room
	5. modify the update API with the same algo to check conflict
	6. 

We have a database for booking a room with 3 field, BookingDate, BookingTimeStart and BookingTimeEnd. How to create a API to check that a newly added booking do not conflict with any others bookings
# 5th day
* Learn how to apply sending email to a service
* add new template for sending email
# 6th
* Learn about the authentication service
## Meeting VGU Booking App Overview

# 7th
Do the log 
learn react
# 8th
Create Log middleware to catch any HTTP request
# 9th
Learn how to map from Log -> LogDTO where userID in log -> Username in LogDTO by 
# 10th
# 11th
[[Follow Up Meeting]]
# 12th
* Làm Facility
	* một phòng có thể có nhiều facility 
* Xem lại bảng Room
# 13th
Mỗi user có 1 hoặc nhiều role, một role chỉ có một list permission 
permission này là permission tới cái gì :V- nếu mà permission(CRUD) tới các bảng khác, thì làm sao để thể hiện cái này 
nối tới 1 bảng khác, ghi list những bảng ảnh hưởng

Bảng Role
* ID
* Name

có một bảng như này **Permission**
- ID
- RoleGuid - role nào
- Table ? ( kiểu bảng nào Booking?, room ?) đại loại z, ID tĩnh 
- 4 quyền
**Nếu các role nó đè lên nhau thì sao ?** -> kiếm nếu có access thì cho, không có thì k cho

CRUD facility cho room 
CRUD facility + search
# 14th
* dropdown để chọn building -> chọn floor -> timeslot -> hiện ra list room
# 15th 
complete the api for the list yesterday
* dropdown building -> pagination
Mỗi người chỉ có 1 role :V

Update Building chưa

	LdapLogin = true


------

Enter -
Login -
Logout -
routing -> booking page - 
Api Room -> Room Function ...
spinner on login 

---
API Xuất report booking ra excel, theo ngày  ( both csv and xlsx)

Join table in booking API - 

# Meeting
 * notification for each user  - about changes in booking (after pres)
 * 23/04 tren test server
 * change the room table -> add field for easy query
 * login func ( after pres)


* Update the working by getting the property dynamically

SearchBooking with Bookingtime - booking status - done
tao database for regulation - done

add the pagination for add the search Function


gop 2 cai login - done

Spinner
Format ngay
them ten vao event
disable may cai vehicle



Khi token con thi ve home,
khi token het han thi login


Sua api conflict
remove toast
remove unnecessary 
add button quick add
add loader



Add more service to recursively delete facility

* onClick room, show facility - add facility
* make the component more organized
* 