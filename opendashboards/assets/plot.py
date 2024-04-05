
import streamlit as st
import opendashboards.utils.plotting as plotting

def timeline(df_runs, color='state'):
    return st.plotly_chart(
        plotting.plot_gantt(df_runs, color=color),
        use_container_width=True
    )
    
# @st.cache_data
def uid_diversty(df, rm_failed=True):
    return st.plotly_chart(
        plotting.plot_uid_diversty(
            df,
            remove_unsuccessful=rm_failed
        ).update_layout(
            coloraxis_showscale=False,
        ),
        use_container_width=True
    )

# @st.cache_data
def leaderboard(df, ntop, group_on, agg_col, agg, alias=False):
    return st.plotly_chart(
        plotting.plot_leaderboard(
            df,
            ntop=ntop,
            group_on=group_on,
            agg_col=agg_col,
            agg=agg,
            alias=alias
        ).update_layout(
            coloraxis_showscale=False,
        ),
        use_container_width=True
    )

# @st.cache_data
def completion_rewards(df, completion_col, reward_col, uid_col, ntop, completions=None, completion_regex=None):
    return st.plotly_chart(
        plotting.plot_completion_rewards(
            df,
            msg_col=completion_col,
            reward_col=reward_col,
            uid_col=uid_col,
            ntop=ntop,
            completions=completions,
            completion_regex=completion_regex
        ),
        use_container_width=True
    )
    
def weights(df, uids, ntop=10):
    return st.plotly_chart(
        plotting.plot_weights(
            df,
            uids=[f'UID-{i}' for i in uids],
            ntop=ntop
        ),
        use_container_width=True
    )

def completion_length_time(df, completion_col, uid_col, time_col, length_opt='characters'):
    return st.plotly_chart(
        plotting.plot_completion_length_time(
            df,
            uid_col=uid_col,
            completion_col=completion_col,
            time_col=time_col,
            length_opt=length_opt
        ),
        use_container_width=True
    )

def uid_completion_counts(df, uids, src, rm_empty, ntop=100, cumulative=False, normalize=True):
    return st.plotly_chart(
        plotting.plot_uid_completion_counts(
            df,
            uids=uids,
            src=src,
            rm_empty=rm_empty,
            ntop=ntop,
            cumulative=cumulative,
            normalize=normalize
        ),
        use_container_width=True
    )