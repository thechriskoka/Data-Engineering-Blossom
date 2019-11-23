create schema stackoverflow_filtered;

SET search_path TO stackoverflow_filtered;

create table results(
		question_id text NOT NULL,
		user_id text NOT NULL PRIMARY KEY,
		display_name text NULL,
		reputation text NULL,
		website_url text NULL,
		"location" text NULL,
		about_me text NULL,
		"views" text NULL,
		up_votes text NULL,
		down_votes text NULL,
		image_url text NULL,
		user_created_at text NULL,
		user_updated_at text NULL,
		city text NULL,
		country text NULL,
		title text NULL,
		question_body text NULL,
		accepted_answer_id text NULL,
		question_score text NULL,
		view_count text NULL,
		comment_count text NULL,
		question_created_at text NULL,
		answer_id text NULL,
		answer_body text NULL,
		answer_score text NULL,
		answer_comment_count text NULL,
		answer_created_at text null		
			 
);

-- creating a btree index on reputation
create index reputation_index on results;

-- creating a hash index on display name
create index display_name on results using hash;

-- creating a view
create view normal_view as 
		select display_name, city, question_id from results
			where accepted_answer_id is not null;
		
-- creating a materialized view
create materialized view  materialized_view as 
		select display_name, city, question_id from results 
			where accepted_answer_id is not null;

		
		
		
