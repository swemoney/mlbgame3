#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mlbgame functions for the people API endpoints.

This module's functions gets the JSON payloads for the mlb.com standings API
endpoints.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""

from mlbgame.data import request

def get_standings(standingsType, params=None):
    """This endpoint allows you to pull standings
    Args:
        params (dict): Contains the season and standingsType
            parameters described below.

    params:
      standingsType (required)
        Description: Type of season. Available types in /api/v1/standingsTypes
        Parameter Type: path
        Data Type: Optional<<string>>
      leagueId (might be required)
        Description: Unique League Identifier Available leagues in /api/v1/leagues
        Format: [103,104] (AL and NL)
        Parameter Type: query
        Data Type: array[integer]
      season
        Description: Season of play
        Parameter Type: query
        Data Type: string
      standingsTypes
        Description: Type of season. Available types in /api/v1/standingsTypes
        Parameter Type: query
        Data Type: array[string]
      date
        Description: Date of Game.
        Format: MM/DD/YYYY
        Parameter Type: query
        Data Type: LocalDate
      teamId
        Description: Unique Team Identifier.
        Format: Format: 141, 147, etc
        Parameter Type: query
        Data Type: integer
      includeMLB
        Description: Determines whether to include major league teams when
            using the 'BY_ORGANIZATION' standings type
        Parameter Type: query
        Data Type: boolean
      fields
        Description: Comma delimited list of specific fields to be returned.
        Format: topLevelNode, childNode, attribute
        Parameter Type: query
        Data Type: array[string]

    Returns:
      json
    """
    return request(11, standingsType, params=params)

def get_standings_types():
    """This endpoint allows you to pull standings
    Currently just returns the json directly

    Returns:
      json
    """

    return [{
      "name" : "regularSeason",
      "description" : "Regular Season Standings"
    }, {
      "name" : "wildCard",
      "description" : "Wild card standings"
    }, {
      "name" : "divisionLeaders",
      "description" : "Division Leader standings"
    }, {
      "name" : "wildCardWithLeaders",
      "description" : "Wild card standings with Division Leaders"
    }, {
      "name" : "firstHalf",
      "description" : "First half standings.  Only valid for leagues with a split season."
    }, {
      "name" : "secondHalf",
      "description" : "Second half standings. Only valid for leagues with a split season."
    }, {
      "name" : "springTraining",
      "description" : "Spring Training Standings"
    }, {
      "name" : "postseason",
      "description" : "Postseason Standings"
    }, {
      "name" : "byDivision",
      "description" : "Standings by Division"
    }, {
      "name" : "byConference",
      "description" : "Standings by Conference"
    }, {
      "name" : "byLeague",
      "description" : "Standings by League"
    }, {
      "name" : "byOrganization",
      "description" : "Standing by Organization"
    }]
