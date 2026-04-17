package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  Enriched NVD representation of a CVE entry.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NVDEntry extends Vulnerability {

  private String descriptionSource;
  private String analysisDescription;
  private MetricSet metrics;
  private List<CPEConfiguration> configurations;
  private List<VendorComment> vendorComments;
  private List<String> nvdTags;
  private List<String> cveTags;
  private String workflowStatus;
  private List<StatusTransition> statusTransitions;
  private KnownExploitedVulnerability knownExploited;
  private String cweView;
  private ZonedDateTime dateReceived;

}