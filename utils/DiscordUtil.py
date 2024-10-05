import configs.DefaultConfig as defaultconfig

def is_me(ctx):
    return ctx.author.id == int(defaultconfig.DISCORD_OWNER_ID)
