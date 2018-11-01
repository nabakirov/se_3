use University
go

create trigger for_insert
	on students for insert
	as insert into dbo.TableForTrigger
		(id, [name], birthday, region_id, nationality_id, group_id, activity)
	select id, [name], birthday, region_id, nationality_id, group_id, 'insert' from inserted
go
create trigger for_update
	on students for update
	as insert into dbo.TableForTrigger
		(id, [name], birthday, region_id, nationality_id, group_id, activity)
	select id, [name], birthday, region_id, nationality_id, group_id, 'update' from inserted
go
create trigger for_delete
	on students for delete
	as insert into dbo.TableForTrigger
		(id, [name], birthday, region_id, nationality_id, group_id, activity)
	select id, [name], birthday, region_id, nationality_id, group_id, 'delete' from deleted

go