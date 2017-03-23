Feature: manipulate databases:
  create, drop, connect, disconnect

  Scenario: create and drop temporary database
     When we run pgcli
      and we wait for prompt
      and we create database
      then we see database created
      when we drop database
      then we see database dropped
      when we connect to postgres
      then we see database connected

  Scenario: connect and disconnect from test database
     When we run pgcli
      and we wait for prompt
      and we connect to test database
      then we see database connected
      when we connect to postgres
      then we see database connected
