FROM kbase/sdkbase2:python
MAINTAINER KBase Developer
# -----------------------------------------
# In this section, you can install any system dependencies required
# to run your App.  For instance, you could place an apt-get update or
# install line here, a git checkout to download code, or run any other
# installation scripts.

RUN apt-get update
RUN apt-get --yes --force-yes install build-essential
RUN apt-get install -y r-base

# -----------------------------------------

RUN mkdir -p /kb/deps
COPY ./deps /kb/deps
RUN echo Making dependency

RUN \
  sh /kb/deps/kb_psl/install-pyseqlogo.sh && \
  sh /kb/deps/kb_mfmd/install-mfmd.sh && \
  sh /kb/deps/kb_meme/install-meme.sh

# -----------------------------------------

COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod -R a+rw /kb/module

WORKDIR /kb/module

RUN make all

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
