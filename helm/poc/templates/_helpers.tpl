{{- define "poc.name" -}}
{{ .Chart.Name }}
{{- end -}}

{{- define "poc.labels" -}}
app.kubernetes.io/name: {{ include "poc.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}
