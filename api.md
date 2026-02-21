# Believe

Methods:

- <code title="get /">client.<a href="./src/believe/_client.py">get_welcome</a>() -> object</code>

# Characters

Types:

```python
from believe.types import (
    Character,
    CharacterRole,
    EmotionalStats,
    GrowthArc,
    CharacterGetQuotesResponse,
)
```

Methods:

- <code title="post /characters">client.characters.<a href="./src/believe/resources/characters.py">create</a>(\*\*<a href="src/believe/types/character_create_params.py">params</a>) -> <a href="./src/believe/types/character.py">Character</a></code>
- <code title="get /characters/{character_id}">client.characters.<a href="./src/believe/resources/characters.py">retrieve</a>(character_id) -> <a href="./src/believe/types/character.py">Character</a></code>
- <code title="patch /characters/{character_id}">client.characters.<a href="./src/believe/resources/characters.py">update</a>(character_id, \*\*<a href="src/believe/types/character_update_params.py">params</a>) -> <a href="./src/believe/types/character.py">Character</a></code>
- <code title="get /characters">client.characters.<a href="./src/believe/resources/characters.py">list</a>(\*\*<a href="src/believe/types/character_list_params.py">params</a>) -> <a href="./src/believe/types/character.py">SyncSkipLimitPage[Character]</a></code>
- <code title="delete /characters/{character_id}">client.characters.<a href="./src/believe/resources/characters.py">delete</a>(character_id) -> None</code>
- <code title="get /characters/{character_id}/quotes">client.characters.<a href="./src/believe/resources/characters.py">get_quotes</a>(character_id) -> <a href="./src/believe/types/character_get_quotes_response.py">CharacterGetQuotesResponse</a></code>

# Teams

Types:

```python
from believe.types import (
    GeoLocation,
    League,
    Team,
    TeamValues,
    TeamGetCultureResponse,
    TeamGetRivalsResponse,
    TeamListLogosResponse,
)
```

Methods:

- <code title="post /teams">client.teams.<a href="./src/believe/resources/teams/teams.py">create</a>(\*\*<a href="src/believe/types/team_create_params.py">params</a>) -> <a href="./src/believe/types/team.py">Team</a></code>
- <code title="get /teams/{team_id}">client.teams.<a href="./src/believe/resources/teams/teams.py">retrieve</a>(team_id) -> <a href="./src/believe/types/team.py">Team</a></code>
- <code title="patch /teams/{team_id}">client.teams.<a href="./src/believe/resources/teams/teams.py">update</a>(team_id, \*\*<a href="src/believe/types/team_update_params.py">params</a>) -> <a href="./src/believe/types/team.py">Team</a></code>
- <code title="get /teams">client.teams.<a href="./src/believe/resources/teams/teams.py">list</a>(\*\*<a href="src/believe/types/team_list_params.py">params</a>) -> <a href="./src/believe/types/team.py">SyncSkipLimitPage[Team]</a></code>
- <code title="delete /teams/{team_id}">client.teams.<a href="./src/believe/resources/teams/teams.py">delete</a>(team_id) -> None</code>
- <code title="get /teams/{team_id}/culture">client.teams.<a href="./src/believe/resources/teams/teams.py">get_culture</a>(team_id) -> <a href="./src/believe/types/team_get_culture_response.py">TeamGetCultureResponse</a></code>
- <code title="get /teams/{team_id}/rivals">client.teams.<a href="./src/believe/resources/teams/teams.py">get_rivals</a>(team_id) -> <a href="./src/believe/types/team_get_rivals_response.py">TeamGetRivalsResponse</a></code>
- <code title="get /teams/{team_id}/logos">client.teams.<a href="./src/believe/resources/teams/teams.py">list_logos</a>(team_id) -> <a href="./src/believe/types/team_list_logos_response.py">TeamListLogosResponse</a></code>

## Logo

Types:

```python
from believe.types.teams import FileUpload
```

Methods:

- <code title="delete /teams/{team_id}/logo/{file_id}">client.teams.logo.<a href="./src/believe/resources/teams/logo.py">delete</a>(file_id, \*, team_id) -> None</code>
- <code title="get /teams/{team_id}/logo/{file_id}">client.teams.logo.<a href="./src/believe/resources/teams/logo.py">download</a>(file_id, \*, team_id) -> object</code>
- <code title="post /teams/{team_id}/logo">client.teams.logo.<a href="./src/believe/resources/teams/logo.py">upload</a>(team_id, \*\*<a href="src/believe/types/teams/logo_upload_params.py">params</a>) -> <a href="./src/believe/types/teams/file_upload.py">FileUpload</a></code>

# Matches

Types:

```python
from believe.types import (
    Match,
    MatchResult,
    MatchType,
    TurningPoint,
    MatchGetLessonResponse,
    MatchGetTurningPointsResponse,
)
```

Methods:

- <code title="post /matches">client.matches.<a href="./src/believe/resources/matches/matches.py">create</a>(\*\*<a href="src/believe/types/match_create_params.py">params</a>) -> <a href="./src/believe/types/match.py">Match</a></code>
- <code title="get /matches/{match_id}">client.matches.<a href="./src/believe/resources/matches/matches.py">retrieve</a>(match_id) -> <a href="./src/believe/types/match.py">Match</a></code>
- <code title="patch /matches/{match_id}">client.matches.<a href="./src/believe/resources/matches/matches.py">update</a>(match_id, \*\*<a href="src/believe/types/match_update_params.py">params</a>) -> <a href="./src/believe/types/match.py">Match</a></code>
- <code title="get /matches">client.matches.<a href="./src/believe/resources/matches/matches.py">list</a>(\*\*<a href="src/believe/types/match_list_params.py">params</a>) -> <a href="./src/believe/types/match.py">SyncSkipLimitPage[Match]</a></code>
- <code title="delete /matches/{match_id}">client.matches.<a href="./src/believe/resources/matches/matches.py">delete</a>(match_id) -> None</code>
- <code title="get /matches/{match_id}/lesson">client.matches.<a href="./src/believe/resources/matches/matches.py">get_lesson</a>(match_id) -> <a href="./src/believe/types/match_get_lesson_response.py">MatchGetLessonResponse</a></code>
- <code title="get /matches/{match_id}/turning-points">client.matches.<a href="./src/believe/resources/matches/matches.py">get_turning_points</a>(match_id) -> <a href="./src/believe/types/match_get_turning_points_response.py">MatchGetTurningPointsResponse</a></code>
- <code title="get /matches/live">client.matches.<a href="./src/believe/resources/matches/matches.py">stream_live</a>(\*\*<a href="src/believe/types/match_stream_live_params.py">params</a>) -> None</code>

## Commentary

Methods:

- <code title="post /matches/{match_id}/commentary/stream">client.matches.commentary.<a href="./src/believe/resources/matches/commentary.py">stream</a>(match_id) -> object</code>

# Episodes

Types:

```python
from believe.types import Episode, PaginatedResponse, EpisodeGetWisdomResponse
```

Methods:

- <code title="post /episodes">client.episodes.<a href="./src/believe/resources/episodes.py">create</a>(\*\*<a href="src/believe/types/episode_create_params.py">params</a>) -> <a href="./src/believe/types/episode.py">Episode</a></code>
- <code title="get /episodes/{episode_id}">client.episodes.<a href="./src/believe/resources/episodes.py">retrieve</a>(episode_id) -> <a href="./src/believe/types/episode.py">Episode</a></code>
- <code title="patch /episodes/{episode_id}">client.episodes.<a href="./src/believe/resources/episodes.py">update</a>(episode_id, \*\*<a href="src/believe/types/episode_update_params.py">params</a>) -> <a href="./src/believe/types/episode.py">Episode</a></code>
- <code title="get /episodes">client.episodes.<a href="./src/believe/resources/episodes.py">list</a>(\*\*<a href="src/believe/types/episode_list_params.py">params</a>) -> <a href="./src/believe/types/episode.py">SyncSkipLimitPage[Episode]</a></code>
- <code title="delete /episodes/{episode_id}">client.episodes.<a href="./src/believe/resources/episodes.py">delete</a>(episode_id) -> None</code>
- <code title="get /episodes/{episode_id}/wisdom">client.episodes.<a href="./src/believe/resources/episodes.py">get_wisdom</a>(episode_id) -> <a href="./src/believe/types/episode_get_wisdom_response.py">EpisodeGetWisdomResponse</a></code>

# Quotes

Types:

```python
from believe.types import PaginatedResponseQuote, Quote, QuoteMoment, QuoteTheme
```

Methods:

- <code title="post /quotes">client.quotes.<a href="./src/believe/resources/quotes.py">create</a>(\*\*<a href="src/believe/types/quote_create_params.py">params</a>) -> <a href="./src/believe/types/quote.py">Quote</a></code>
- <code title="get /quotes/{quote_id}">client.quotes.<a href="./src/believe/resources/quotes.py">retrieve</a>(quote_id) -> <a href="./src/believe/types/quote.py">Quote</a></code>
- <code title="patch /quotes/{quote_id}">client.quotes.<a href="./src/believe/resources/quotes.py">update</a>(quote_id, \*\*<a href="src/believe/types/quote_update_params.py">params</a>) -> <a href="./src/believe/types/quote.py">Quote</a></code>
- <code title="get /quotes">client.quotes.<a href="./src/believe/resources/quotes.py">list</a>(\*\*<a href="src/believe/types/quote_list_params.py">params</a>) -> <a href="./src/believe/types/quote.py">SyncSkipLimitPage[Quote]</a></code>
- <code title="delete /quotes/{quote_id}">client.quotes.<a href="./src/believe/resources/quotes.py">delete</a>(quote_id) -> None</code>
- <code title="get /quotes/random">client.quotes.<a href="./src/believe/resources/quotes.py">get_random</a>(\*\*<a href="src/believe/types/quote_get_random_params.py">params</a>) -> <a href="./src/believe/types/quote.py">Quote</a></code>
- <code title="get /quotes/characters/{character_id}">client.quotes.<a href="./src/believe/resources/quotes.py">list_by_character</a>(character_id, \*\*<a href="src/believe/types/quote_list_by_character_params.py">params</a>) -> <a href="./src/believe/types/quote.py">SyncSkipLimitPage[Quote]</a></code>
- <code title="get /quotes/themes/{theme}">client.quotes.<a href="./src/believe/resources/quotes.py">list_by_theme</a>(theme, \*\*<a href="src/believe/types/quote_list_by_theme_params.py">params</a>) -> <a href="./src/believe/types/quote.py">SyncSkipLimitPage[Quote]</a></code>

# Believe

Types:

```python
from believe.types import BelieveSubmitResponse
```

Methods:

- <code title="post /believe">client.believe.<a href="./src/believe/resources/believe.py">submit</a>(\*\*<a href="src/believe/types/believe_submit_params.py">params</a>) -> <a href="./src/believe/types/believe_submit_response.py">BelieveSubmitResponse</a></code>

# Conflicts

Types:

```python
from believe.types import ConflictResolveResponse
```

Methods:

- <code title="post /conflicts/resolve">client.conflicts.<a href="./src/believe/resources/conflicts.py">resolve</a>(\*\*<a href="src/believe/types/conflict_resolve_params.py">params</a>) -> <a href="./src/believe/types/conflict_resolve_response.py">ConflictResolveResponse</a></code>

# Reframe

Types:

```python
from believe.types import ReframeTransformNegativeThoughtsResponse
```

Methods:

- <code title="post /reframe">client.reframe.<a href="./src/believe/resources/reframe.py">transform_negative_thoughts</a>(\*\*<a href="src/believe/types/reframe_transform_negative_thoughts_params.py">params</a>) -> <a href="./src/believe/types/reframe_transform_negative_thoughts_response.py">ReframeTransformNegativeThoughtsResponse</a></code>

# Press

Types:

```python
from believe.types import PressSimulateResponse
```

Methods:

- <code title="post /press">client.press.<a href="./src/believe/resources/press.py">simulate</a>(\*\*<a href="src/believe/types/press_simulate_params.py">params</a>) -> <a href="./src/believe/types/press_simulate_response.py">PressSimulateResponse</a></code>

# Coaching

## Principles

Types:

```python
from believe.types.coaching import CoachingPrinciple
```

Methods:

- <code title="get /coaching/principles/{principle_id}">client.coaching.principles.<a href="./src/believe/resources/coaching/principles.py">retrieve</a>(principle_id) -> <a href="./src/believe/types/coaching/coaching_principle.py">CoachingPrinciple</a></code>
- <code title="get /coaching/principles">client.coaching.principles.<a href="./src/believe/resources/coaching/principles.py">list</a>(\*\*<a href="src/believe/types/coaching/principle_list_params.py">params</a>) -> <a href="./src/believe/types/coaching/coaching_principle.py">SyncSkipLimitPage[CoachingPrinciple]</a></code>
- <code title="get /coaching/principles/random">client.coaching.principles.<a href="./src/believe/resources/coaching/principles.py">get_random</a>() -> <a href="./src/believe/types/coaching/coaching_principle.py">CoachingPrinciple</a></code>

# Biscuits

Types:

```python
from believe.types import Biscuit
```

Methods:

- <code title="get /biscuits/{biscuit_id}">client.biscuits.<a href="./src/believe/resources/biscuits.py">retrieve</a>(biscuit_id) -> <a href="./src/believe/types/biscuit.py">Biscuit</a></code>
- <code title="get /biscuits">client.biscuits.<a href="./src/believe/resources/biscuits.py">list</a>(\*\*<a href="src/believe/types/biscuit_list_params.py">params</a>) -> <a href="./src/believe/types/biscuit.py">SyncSkipLimitPage[Biscuit]</a></code>
- <code title="get /biscuits/fresh">client.biscuits.<a href="./src/believe/resources/biscuits.py">get_fresh</a>() -> <a href="./src/believe/types/biscuit.py">Biscuit</a></code>

# PepTalk

Types:

```python
from believe.types import PepTalkRetrieveResponse
```

Methods:

- <code title="get /pep-talk">client.pep_talk.<a href="./src/believe/resources/pep_talk.py">retrieve</a>(\*\*<a href="src/believe/types/pep_talk_retrieve_params.py">params</a>) -> <a href="./src/believe/types/pep_talk_retrieve_response.py">PepTalkRetrieveResponse</a></code>

# Stream

Methods:

- <code title="get /stream/test">client.stream.<a href="./src/believe/resources/stream.py">test_connection</a>() -> object</code>

# TeamMembers

Types:

```python
from believe.types import (
    Coach,
    CoachSpecialty,
    EquipmentManager,
    MedicalSpecialty,
    MedicalStaff,
    Player,
    Position,
    TeamMemberCreateResponse,
    TeamMemberRetrieveResponse,
    TeamMemberUpdateResponse,
    TeamMemberListResponse,
    TeamMemberListStaffResponse,
)
```

Methods:

- <code title="post /team-members">client.team_members.<a href="./src/believe/resources/team_members.py">create</a>(\*\*<a href="src/believe/types/team_member_create_params.py">params</a>) -> <a href="./src/believe/types/team_member_create_response.py">TeamMemberCreateResponse</a></code>
- <code title="get /team-members/{member_id}">client.team_members.<a href="./src/believe/resources/team_members.py">retrieve</a>(member_id) -> <a href="./src/believe/types/team_member_retrieve_response.py">TeamMemberRetrieveResponse</a></code>
- <code title="patch /team-members/{member_id}">client.team_members.<a href="./src/believe/resources/team_members.py">update</a>(member_id, \*\*<a href="src/believe/types/team_member_update_params.py">params</a>) -> <a href="./src/believe/types/team_member_update_response.py">TeamMemberUpdateResponse</a></code>
- <code title="get /team-members">client.team_members.<a href="./src/believe/resources/team_members.py">list</a>(\*\*<a href="src/believe/types/team_member_list_params.py">params</a>) -> <a href="./src/believe/types/team_member_list_response.py">SyncSkipLimitPage[TeamMemberListResponse]</a></code>
- <code title="delete /team-members/{member_id}">client.team_members.<a href="./src/believe/resources/team_members.py">delete</a>(member_id) -> None</code>
- <code title="get /team-members/coaches/">client.team_members.<a href="./src/believe/resources/team_members.py">list_coaches</a>(\*\*<a href="src/believe/types/team_member_list_coaches_params.py">params</a>) -> <a href="./src/believe/types/coach.py">SyncSkipLimitPage[Coach]</a></code>
- <code title="get /team-members/players/">client.team_members.<a href="./src/believe/resources/team_members.py">list_players</a>(\*\*<a href="src/believe/types/team_member_list_players_params.py">params</a>) -> <a href="./src/believe/types/player.py">SyncSkipLimitPage[Player]</a></code>
- <code title="get /team-members/staff/">client.team_members.<a href="./src/believe/resources/team_members.py">list_staff</a>(\*\*<a href="src/believe/types/team_member_list_staff_params.py">params</a>) -> <a href="./src/believe/types/team_member_list_staff_response.py">SyncSkipLimitPage[TeamMemberListStaffResponse]</a></code>

# Webhooks

Types:

```python
from believe.types import (
    RegisteredWebhook,
    WebhookCreateResponse,
    WebhookListResponse,
    WebhookDeleteResponse,
    WebhookTriggerEventResponse,
    MatchCompletedWebhookEvent,
    TeamMemberTransferredWebhookEvent,
    UnwrapWebhookEvent,
)
```

Methods:

- <code title="post /webhooks">client.webhooks.<a href="./src/believe/resources/webhooks.py">create</a>(\*\*<a href="src/believe/types/webhook_create_params.py">params</a>) -> <a href="./src/believe/types/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="get /webhooks/{webhook_id}">client.webhooks.<a href="./src/believe/resources/webhooks.py">retrieve</a>(webhook_id) -> <a href="./src/believe/types/registered_webhook.py">RegisteredWebhook</a></code>
- <code title="get /webhooks">client.webhooks.<a href="./src/believe/resources/webhooks.py">list</a>() -> <a href="./src/believe/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /webhooks/{webhook_id}">client.webhooks.<a href="./src/believe/resources/webhooks.py">delete</a>(webhook_id) -> <a href="./src/believe/types/webhook_delete_response.py">WebhookDeleteResponse</a></code>
- <code title="post /webhooks/trigger">client.webhooks.<a href="./src/believe/resources/webhooks.py">trigger_event</a>(\*\*<a href="src/believe/types/webhook_trigger_event_params.py">params</a>) -> <a href="./src/believe/types/webhook_trigger_event_response.py">WebhookTriggerEventResponse</a></code>

# Health

Methods:

- <code title="get /health">client.health.<a href="./src/believe/resources/health.py">check</a>() -> object</code>

# Version

Methods:

- <code title="get /version">client.version.<a href="./src/believe/resources/version.py">retrieve</a>() -> object</code>
