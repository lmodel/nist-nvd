package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  State transition event in NVD enrichment workflow.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class StatusTransition  {

  private String transitionId;
  private String fromStatus;
  private String toStatus;
  private String eventSource;
  private ZonedDateTime transitionTime;
  private String rationale;

}