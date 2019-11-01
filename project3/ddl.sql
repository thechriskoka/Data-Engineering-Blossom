create schema stackoverflow_filtered;

create table results(
	  user_id text NOT null,
	  question_id text NOT null,
	  title text NOT null,
	  question_body text NOT null,
	  accepted_answer_id text NOT null,
	  question_score text NOT null,
	  view_count text NOT null,
	  question_comment_count text NOT null,
	  question_created_at text NOT null,
	  display_name text NOT null,
	  reputation text NOT null,
	  website_url text NOT null,
	  "location"text NOT null,
	  about_me text NOT null,
	  "views" text NOT null,
	  up_votes text NOT null,
	  down_votes text NOT null,
	  image_url text NOT null,
	  created_at text NOT null,
	  updated_at text NOT null,
	  city text NOT null,
	  country text NOT null,
	  answer_id text NOT null,
	  ans_question_id text NOT null,
	  answer_body text NOT null,
	  answer_score text NOT NULL,
	  answer_comment_count text NOT null,
	  answer_created_at text NOT null
	
);


