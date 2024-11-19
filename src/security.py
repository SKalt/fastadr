from typing import Annotated, Any
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2, SecurityScopes
from fastapi.openapi.models import OAuthFlows, OAuthFlowClientCredentials
from starlette.status import HTTP_401_UNAUTHORIZED
import jwt


class OAuth2ClientCredentials(OAuth2): ...


oauth2_scheme = OAuth2(
    scheme_name="oAuth2ClientCredentials",
    flows=OAuthFlows(
        # TODO: allow VENs and users to authenticate with authorization code
        clientCredentials=OAuthFlowClientCredentials(
            tokenUrl="/token",  # FIXME: make configurable
            refreshUrl="/token",  # FIXME: make configurable
            scopes={
                "read_all": "VENs and BL can read all resources",
                "write_programs": "Only BL can write to programs",
                "write_events": "Only BL can write to events",
                "write_reports": "only VENs can write to reports",
                "write_subscriptions": "VENs and BL can write to subscriptions",
                "write_vens": "VENS and BL can write to vens and resources",
            },
        )
    ),
)

jwk_url = "https://TODO/.well-known/jwks.json"
jwks = jwt.PyJWKClient(jwk_url)


def check_auth(
    security_scopes: SecurityScopes, token: Annotated[str, Depends(oauth2_scheme)]
) -> dict[str, Any]:
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"
    err = HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        jwk = jwks.get_signing_key_from_jwt(token)
        decoded: dict[str, Any] = jwt.decode(  # type: ignore # FIXME
            token,
            jwk,
            algorithms=["RS256"],
            # TODO: use ed25519: "EdDSA" # https://stackoverflow.com/questions/66893790/alg-value-for-ed25519
            audiences=["TODO"],  # TODO: make configurable
            verify=True,
        )
    except (jwt.InvalidTokenError, jwt.InvalidAudienceError):
        raise err

    missing_scopes = sorted(set(security_scopes.scopes) - set(decoded.get("scope", [])))
    if missing_scopes:
        raise err
    return decoded


def get_bearer_id(
    security_scopes: SecurityScopes, token: Annotated[str, Depends(oauth2_scheme)]
) -> str:
    decoded = check_auth(security_scopes, token)
    return decoded["sub"]
